from django.urls import path
from . import views

from django.contrib import admin
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('books/', views.get_books, name='get_books'),
    path('book_detail/<int:book_id>/', views.book_detail, name='book_detail'),
]
