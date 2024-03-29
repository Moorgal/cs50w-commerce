from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("my_listings", views.my_listings, name="my_listings"),
    path('listing/<str:pk>/', views.single_page, name="single_page"),
    path('create-listing/', views.createListing, name="create_listing"),
    path('create_comment/<str:pk>', views.create_comment, name="create_comment"),
    path('create_bid/<str:pk>', views.create_bid, name='create_bid'),
    path('close-auction/<str:pk>', views.close_auction, name="close_auction"),
    path('addToWatchList/<str:pk>', views.addToWatchList, name="addToWatchList"),
    path('removeFromWatchList/<str:pk>', views.removeFromWatchList, name="removeFromWatchList"),
    path('mywatchlist/', views.my_watchlist, name="my_watchlist"),
    path('update-listing/<str:pk>/', views.updateListing, name="update-listing"),
    path('delete-listing/<str:pk>/', views.deleteListing, name="delete-listing"),
    path('choose_category/<str:pk>', views.choose_category, name="choose_category"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
