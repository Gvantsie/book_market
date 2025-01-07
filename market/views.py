from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect

from market.forms import UserRegistrationForm, LoginForm
from market.models import Book, Category, Author, User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def get_books(request):
    book_list = Book.objects.filter(stock__gt=0).order_by('title')
    paginator = Paginator(book_list, 4)

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

    return render(request, 'filtered_authors.html', {'books': books, 'selected_author': selected_author, 'authors': authors})


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
