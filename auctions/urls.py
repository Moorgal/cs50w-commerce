from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("books", views.books, name="books"),
    path('listing/<str:pk>/', views.single_page, name="single_page"),
    path('create-listing/', views.createListing, name="create_listing"),
    path('update-listing/<str:pk>/', views.updateListing, name="update-listing"),
    path('delete-listing/<str:pk>/', views.deleteListing, name="delete-listing"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
