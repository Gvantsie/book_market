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

### Book Model   
The app includes a Book model with the following fields:

- `name`: The title of the book.
- `author`: The name of the book's author.
- `categories`: The book's categories.
- `description`: A brief description of the book.
- `best_seller`: A boolean field indicating whether the book is a bestseller.
- `age_group`: The age group for which the book is intended.
- `price`: The price of the book.
- `stock`: The number of copies of the book in stock.
- `cover`: The image file associated with the book cover.
- `cover_type`: The type of the book cover.

### Admin Interface
The Book model is registered in the Django admin interface. The admin list view includes a search field that allows 
searching for books by title and author's name and sorting by bestseller status and price. The admin detail view 
includes a link to view the book's detail page on the site. At the Catalog page, you can survey all books in the catalog.
filter them by categories and Authors.

### Author Model
The Author model is added to the project with properties:

- `first_name`: The first name of the author.
- `last_name`: The last name of the author.
- `date_of_birth`: The author's date of birth.
- `date_of_death`: The author's date of death.
Author model establishes a one-to-many relationship with the Book model.

### Category Model
The Category model is added to the project with properties:

- `id`: The unique identifier of the category in the database.
- `category_name`: The name of the category.
Category model establishes a many-to-many relationship with the Book model.

### Views
The app provides views for book listing and book detail pages, as well as filtered views for categories and authors.

- Book Listing View: This view displays a list of all books in the catalog. I added pagination to the view to limit the 
number of books displayed per page(3 books per page).
- Book Detail View: This view shows detailed information about a single book. The book data is returned in JSON format.
- Category View: This view displays a list of books filtered by category.
- Author View: This view displays a list of books filtered by author.

### URLs
The views are registered in the project's URL patterns:

- `book/ - Book` Listing View, which displays all books in the catalog.
- `book_detail/<int:book_id>/` - Book Detail View, where pk is the primary key of the book. 
- `filtered_books/` - Category View, which displays books filtered by matching category.
- `filtered_authors/` - Author View, which displays books filtered by matching author.

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
The Server of my project will run at http://127.0.0.1:8000/.

### Admin Interface
If you created a superuser:
```bash
python manage.py createsuperuser
```
You will get a chance to open django administrator at http://127.0.0.1:8000/admin/, here you can use add, edit, and 
delete books, Authors and Categories from the catalog or manage other site content.

### Home Page
The `home page` displays a welcome message and a link to the book listing view.
By pressing the `Browse Books` button, you will be redirected to the book catalog view.
My projects interface looks like this:   

### Catalog Page
The `catalog page` displays a list of all books in the catalog. Each book is displayed with its title, 
author, and cover image.
You can click on a book to view its detail page.

### Book Detail Page
The `book detail page` displays detailed information about a single book. The page includes the book's title, author, 
description, price, and stock. You can also view the book's cover image.


### Filtered Books Page
The `filtered books page` displays a list of books filtered by category. The page includes a list of books that match the selected category.   


### Filtered Authors Page
The `filtered authors page` displays a list of books filtered by author. The page includes a list of books that match the selected author.

### Endpoints
The app provides endpoints:
- http://localhost:8000/ - Home Page
- http://localhost:8000/book/ - Book Catalog View
- http://localhost:8000/book_detail/<int:book_id>/ - Book Detail View
- http://localhost:8000/admin/ - Admin Interface
- http://localhost:8000/filtered_books/?category_id=<int:category_id> - Filtered Books View
- http://localhost:8000/filtered_authors/?author_id=<int:author_id> - Filtered Authors View


>>Gvantsa
