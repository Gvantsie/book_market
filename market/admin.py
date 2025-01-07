from django.contrib import admin
from market.models import Book, Author, Category, User, Wishlist

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    search_fields = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    list_filter = ('category_name',)
    search_fields = ('category_name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'stock')
    list_filter = ('title', 'author', 'best_seller', 'categories')
    search_fields = ('title', 'author', 'price', 'categories')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'password')
    list_filter = ('first_name', 'last_name', 'email', 'password')
    search_fields = ('first_name', 'last_name', 'email', 'password')


@admin.register(Wishlist)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('user', 'book')
    list_filter = ('user', 'book')
    search_fields = ('user', 'book')

