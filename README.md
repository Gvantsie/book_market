## Bookstore Project
This is a Django-based web application for a bookstore. The project includes a market app that manages the book catalog.

### Prerequisites
- Python 3.x
- Django 3.x


### Getting Started
1. Clone the repository:
```bash
git clone https://github.com/Gvantsie/book_market.git
```
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```
3. Run the Django development server:
```bash
python manage.py runserver
```
The application should now be accessible at http://127.0.0.1:8000/.

### Market App
The market app is responsible for managing the book catalog in the Bookstore project.

Book Model   
The app includes a Book model with the following fields:

- `name`: The title of the book.
- `author_name`: The name of the book's author.
- `description`: A brief description of the book.
- `best_seller`: A boolean field indicating whether the book is a bestseller.
- `age_group`: The age group for which the book is intended.
- `category`: The category or genre of the book.
- `price`: The price of the book.
- `stock`: The number of copies of the book in stock.
- `cover`: The image file associated with the book cover.

### Admin Interface
The Book model is registered in the Django admin interface. The admin list view includes a search field that allows 
searching for books by title and author's name and sorting by bestseller status and price. The admin detail view 
includes a link to view the book's detail page on the site.

### Views
The app provides two views:

- Book Listing View: This view displays a list of all books in the catalog. I added pagination to the view to limit the 
number of books displayed per page(3 books per page).
- Book Detail View: This view shows detailed information about a single book. The book data is returned in JSON format.

### URLs
The views are registered in the project's URL patterns:

- `book/ - Book` Listing View, which displays all books in the catalog.
- `book/<int:pk>/` - Book Detail View, where pk is the primary key of the book.

### Running the Project

1. Apply the database migrations:
```bash
python manage.py migrate
```
2. Create a superuser for the admin interface:
```bash
python manage.py createsuperuser
```
3.Run the development server:
```bash
python manage.py runserver
```
The application should now be accessible at http://127.0.0.1:8000/.

### Admin Interface
If you created a superuser, you can access the admin interface at http://127.0.0.1:8000/admin/. You can use the admin to
add, edit, and delete books from the catalog or manage other site content.

### Home Page
The `home page` displays a welcome message and a link to the book listing view.
By pressing the `Browse Books` button, you will be redirected to the book catalog view.

### Catalog Page
The `catalog page` displays a list of all books in the catalog. Each book is displayed with its title, author, and cover image.
You can click on a book to view its detail page.

### Book Detail Page
The `book detail page` displays detailed information about a single book. The page includes the book's title, author, description, price, and stock. You can also view the book's cover image.

### Endpoints
The app provides endpoints:
http://localhost:8000/ - Home page View
http://localhost:8000/book/ - Book Catalog View
http://localhost:8000/api/book/<int:pk>/ - Book Detail View
http://localhost:8000/admin/ - Admin Interface
