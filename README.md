# Library Management System

This is a Library Management System built with Django. It allows users to borrow and return books, and manage user information.

## Prerequisites

- Python 3.x
- Django 3.x or higher
- pip (Python package installer)
- Git (optional, for cloning the repository)
- SQLite3 (for database management)

## Setup Instructions

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository

If you have Git installed, you can clone the repository using the following command:

```bash
git clone <repository-url>
```

Alternatively, you can download the ZIP file from the repository and extract it.

### 2. Navigate to the Project Directory

```bash
cd library_management
```

### 3. Create a Virtual Environment

It is recommended to create a virtual environment to manage dependencies. Run the following commands:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 4. Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### 5. Install SQLite3

Download and install SQLite3 from the official website: [SQLite Download Page](https://www.sqlite.org/download.html).

After installation, add the SQLite3 executable to your system PATH:

- **Windows**: Add the path to the SQLite3 executable to the `Path` environment variable.
- **Mac/Linux**: Ensure the SQLite3 executable is in your system's PATH.

### 6. Create a `.env` File

Create a `.env` file in the root directory of the project and add the following line:

```dotenv
DJANGO_SECRET_KEY='your-secret-key'
```

Replace `'your-secret-key'` with your actual secret key.

### 7. Create a Database

Open a terminal or command prompt and run the following command to create a new SQLite database named `library_book`:

```bash
sqlite3 library_book.db
```

This will create a new file named `library_book.db` in your current directory.

### 8. Configure SQLite Database

By default, Django uses SQLite as the database. Ensure that the `DATABASES` setting in `settings.py` is configured to use SQLite:

```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'library_book.db',
    }
}
```

### 9. Apply Migrations

Apply the database migrations to set up the database schema:

```bash
python manage.py migrate
```

### 10. Create a Superuser

Create a superuser to access the Django admin interface:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the superuser account.

### 11. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Open your web browser and navigate to `http://127.0.0.1:8000` to access the application.

### 12. Access the Admin Interface

To access the Django admin interface, go to `http://127.0.0.1:8000/admin` and log in with the superuser credentials you created earlier.

## Project Structure

- `library_management/`: Main project directory
- `library/`: Django app for managing books and user information
- `templates/`: HTML templates for the application
- `static/`: Static files (CSS, JavaScript, images)
- `requirements.txt`: List of Python dependencies

## Customization

You can customize the project by modifying the templates, static files, and Django views. Refer to the Django documentation for more information on how to work with Django projects.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
