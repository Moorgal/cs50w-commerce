from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, Listing, Categories, Comments, Bids
from .forms import ListingForm, CommentForm


def index(request):
    listings = Listing.objects.filter(is_available=True)
    category = Categories.objects.all()
    context = {'listings': listings,
               'category': category,
               'site': 'All listings',}
    return render(request, "auctions/index.html", context)

def choose_category(request, pk):
        chosen_category = Categories.objects.get(id=pk)
        the_category = Categories.objects.filter(title__iexact=chosen_category).first()
        listings = Listing.objects.filter(is_available=True, category=the_category)
        category = Categories.objects.all()
        context = {'listings': listings,
               'category': category,
               'site': chosen_category}
        return render(request, "auctions/index.html", context)


def my_listings(request):
    currentUser = request.user
    listings = Listing.objects.filter(user = currentUser)
    context = {"listings": listings, 'site': 'My listings'}
    return render(request, "auctions/watchlist.html", context)

def single_page(request, pk):
    page = Listing.objects.get(id=pk)
    is_verified = request.user in page.watchlist.all()
    comment = Comments.objects.filter(listing_id=pk)
    bids = Bids.objects.filter(listing_id=pk)
    # if no bid yet then false, otherwise check who is the user who bid last
    if not bids:
        last_bid_user = False
    else:
        last_bid_user = bids.latest('date').user_id

    context = {'page': page,
               'is_verified': is_verified,
               'comment': comment,
               'bids':bids,
               'last_bid_user':last_bid_user}
    return render(request, "auctions/single_page.html", context)

def addToWatchList(request, pk):
    data = Listing.objects.get(id=pk)
    data.watchlist.add(request.user)
    return HttpResponseRedirect(reverse('single_page', args=(data.pk,)))

def my_watchlist(request):
    currentUser = request.user
    # watchlist refers back to all users on that list (refered name in models.py)
    listings = currentUser.watchlist.all()
    context = {"listings": listings, 'site': 'Watchlist'}
    return render(request, "auctions/watchlist.html", context)

def removeFromWatchList(request, pk):
    data = Listing.objects.get(id=pk)
    data.watchlist.remove(request.user)
    return HttpResponseRedirect(reverse('single_page', args=(data.pk,)))

def close_auction(request, pk):
    auction = Listing.objects.get(id=pk)
    auction.is_available = False
    auction.save()
    return HttpResponseRedirect(reverse('single_page', args=(auction.pk,)))



def create_comment(request, pk):
    listing = Listing.objects.get(id=pk)
    user = request.user
    body = request.POST['body']

    Comments(
        user_id=user,
        listing_id=listing,
        body=body,
    ).save()
    return HttpResponseRedirect(reverse('single_page', args=(listing.pk,)))

def create_bid(request, pk):
    listing = Listing.objects.get(id=pk)
    user = request.user
    amount = int(request.POST['amount'])
    old_amount = listing.listing_price
    if amount > old_amount:
        Bids(
        user_id=user,
        listing_id=listing,
        amount=amount,
        ).save()
        listing.listing_price = amount
        listing.save()

        page = Listing.objects.get(id=pk)
        is_verified = request.user in page.watchlist.all()
        comment = Comments.objects.filter(listing_id=pk)
        bids = Bids.objects.filter(listing_id=pk)
        context = {'page': page,
               'is_verified': is_verified,
               'comment': comment,
               'bids':bids,
               'message': "success"}
        return render(request, "auctions/single_page.html", context)
    else:
        page = Listing.objects.get(id=pk)
        is_verified = request.user in page.watchlist.all()
        comment = Comments.objects.filter(listing_id=pk)
        bids = Bids.objects.filter(listing_id=pk)
        context = {'page': page,
               'is_verified': is_verified,
               'comment': comment,
               'bids':bids,
               'message': "Bid must be higher then listing price"}
        return render(request, "auctions/single_page.html", context)
    

def createListing(request):
    form = ListingForm()

    if request.method == 'POST':
        owner = Listing(user=request.user)
        form = ListingForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'auctions/listing_form.html', context)


def updateListing(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'auctions/listing_form.html', context)



def deleteListing(request, pk):
    listing = Listing.objects.get(id=pk)
    if request.method == 'POST':
        listing.delete()
        return redirect('index')
    context = {'listing': listing}
    return render(request, 'auctions/delete_template.html', context)



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
