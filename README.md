## Bookstore Project
This is a Django-based web application for a bookstore. The project includes a market app that manages the book catalog.

### Prerequisites
- Python 3.x
- Django 3.x


### Getting Started
1. Clone the repository:
```bash
git clone 
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

- name: The title of the book.
- page_count: The number of pages in the book.
- category: The category or genre of the book.
- author_name: The name of the book's author.
- price: The price of the book.
- image: The image file associated with the book.

### Admin Interface
The Book model is registered in the Django admin interface. The admin list view includes a search field that allows 
searching for books by title and author's name.

### Views
The app provides two views:

Book Listing View: This view displays a list of all books in the catalog.
Book Detail View: This view shows detailed information about a single book. The book data is returned in JSON format.
URLs
The views are registered in the project's URL patterns:

market/ - Book Listing View
market/<int:pk>/ - Book Detail View
Running the Project

Apply the database migrations:
python manage.py migrate
Create a superuser for the admin interface:
python manage.py createsuperuser
Run the development server:

python manage.py runserver
The application should now be accessible at http://127.0.0.1:8000/.
Please note that this asgi.pyREADME.md file assumes you are
deployment, you would need to update the instructions accordingly.
