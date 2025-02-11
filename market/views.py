import json

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from market.forms import UserRegistrationForm, LoginForm
from market.models import Book, Category, Author, User, Wishlist, Cart
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def get_books(request):
    book_list = Book.objects.filter(stock__gt=0).order_by('title')
    paginator = Paginator(book_list, 4)

    books_in_wishlist = []
    books_in_cart = []
    if request.user.is_authenticated:
        books_in_wishlist = Wishlist.objects.filter(user=request.user).values_list('book_id', flat=True)
        books_in_cart = Cart.objects.filter(user=request.user).values_list('book_id', flat=True)

    page_number = request.GET.get('page')
    try:
        books = paginator.page(page_number)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    context = {
        'books': books,
        'books_in_wishlist': list(books_in_wishlist),
        'books_in_cart': list(books_in_cart),
    }

    return render(request, 'book_catalog.html', context)


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})


def filtered_books(request):
    category_id = request.GET.get('category_id')
    selected_category = None
    books = Book.objects.all()

    if category_id:
        selected_category = get_object_or_404(Category, pk=category_id)
        books = books.filter(categories=selected_category)

    return render(request, 'filtered_books.html', {'books': books, 'selected_category': selected_category})


def filtered_authors(request):
    author_id = request.GET.get('author_id')
    selected_author = None
    books = Book.objects.all()
    authors = Author.objects.all()

    if author_id:
        selected_author = get_object_or_404(Author, pk=author_id)
        books = books.filter(author=selected_author)

    return render(request, 'filtered_authors.html',
                  {'books': books, 'selected_author': selected_author, 'authors': authors})


def create_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully.')
            return redirect('login_')
    else:
        form = UserRegistrationForm()
    return render(request, 'create_user.html', {'form': form})


def login_(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            # Authenticate and login the user
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Logged in successfully.')
            return redirect('get_books')  # Redirect to home or another page after login
        else:
            messages.error(request, 'Invalid credentials, please try again.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login_')


@login_required
def toggle_wishlist(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(data)  # Add this to see the content of the request
            book_id = data.get("book_id")
            book = get_object_or_404(Book, pk=book_id)
            user = request.user
            wishlist, created = Wishlist.objects.get_or_create(user=user, book=book)
            if not created:
                wishlist.delete()
                return JsonResponse({"message": "Book removed from wishlist"})
            return JsonResponse({"message": "Book added to wishlist"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)


def wishlist_view(request):
    # Get the wishlist of the current logged-in user
    wishlist_items = Wishlist.objects.filter(user=request.user)
    books_in_wishlist = [item.book for item in wishlist_items]  # Get the books from the wishlist items
    books = Book.objects.all()

    return render(request, 'wishlist.html', {
        'books_in_wishlist': books_in_wishlist,
        'books': books
    })


def remove_from_wishlist(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    wishlist = Wishlist.objects.filter(user=request.user,
                                       book=book).first()  # Get the wishlist item for the specific book
    if wishlist:
        wishlist.delete()  # Delete the wishlist entry
    return redirect('wishlist')  # Redirect to the wishlist page


@login_required
def toggle_cart(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            book_id = data.get("book_id")
            book = get_object_or_404(Book, pk=book_id)
            user = request.user

            cart_item, created = Cart.objects.get_or_create(user=user, book=book)
            if not created:
                cart_item.delete()
                return JsonResponse({"message": "Book removed from cart"})
            return JsonResponse({"message": "Book added to cart"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)


def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    books_in_cart = [item.book for item in cart_items]
    books = Book.objects.all()

    return render(request, 'cart.html', {
        'books_in_cart': books_in_cart,
        'books': books
    })