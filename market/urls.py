from django.urls import path
from . import views

from django.contrib import admin
from .views import filtered_books, filtered_authors

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_books, name='get_books'),
    path('book_detail/<int:book_id>/', views.book_detail, name='book_detail'),
    path('filtered_books/', filtered_books, name='filtered_books'),
    path('filtered_authors/', filtered_authors, name='filtered_authors'),
]
