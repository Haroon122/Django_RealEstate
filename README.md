# Real Estate Website

A Django-based real estate website where users can browse property listings, contact realtors, and manage their property listings.

## Features

- Property listing with detailed information
- User registration and authentication
- Admin dashboard for property management
- Property search functionality
- Contact form for inquiries
- Responsive design

## Technologies Used

- Python 3.13
- Django 5.1.7
- MySQL Database
- Bootstrap 4
- jQuery

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd django-dep-master
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure the database in settings.py

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## Deployment

This project is configured for deployment on PythonAnywhere. See deployment instructions in the documentation.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/) 