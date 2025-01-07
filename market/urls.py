from django.urls import path
from . import views

from django.contrib import admin
from .views import filtered_books, filtered_authors, toggle_wishlist

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_books, name='get_books'),
    path('book_detail/<int:book_id>/', views.book_detail, name='book_detail'),
    path('filtered_books/', filtered_books, name='filtered_books'),
    path('filtered_authors/', filtered_authors, name='filtered_authors'),
    path('register/', views.create_user, name='create_user'),
    path('login/', views.login_, name='login_'),
    path('logout/', views.logout_view, name='logout_'),
    # path('wishlist/<int:book_id>/', views.toggle_wishlist, name='toggle_wishlist'),
    path("wishlist/toggle/", views.toggle_wishlist, name="toggle_wishlist"),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('wishlist/remove/<int:book_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]
