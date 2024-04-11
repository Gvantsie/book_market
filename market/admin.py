from django.contrib import admin
from market.models import Book

# Register your models here.
# admin.site.register(Book)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'stock')
    list_filter = ('title', 'author', 'best_seller', 'category')
    search_fields = ('title', 'author', 'price', 'category')


def site(request):
    return None
