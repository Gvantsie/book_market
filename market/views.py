from django.shortcuts import render, get_object_or_404
from market.models import Book
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def home(request):
    return render(request, 'home.html')


def get_books(request):
    book_list = Book.objects.all().filter(stock__gt=0).order_by('title')
    paginator = Paginator(book_list, 3)

    page_number = request.GET.get('page')
    try:
        books = paginator.page(page_number)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'book_catalog.html', {'books': books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})
