## Badges
[![HTML](https://img.shields.io/badge/HTML-5-red)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS](https://img.shields.io/badge/CSS-3-blue)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-4-purple)](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
[![Django](https://img.shields.io/badge/Django-3.0-green)](https://docs.djangoproject.com/en/3.0/)
[![SQLite](https://img.shields.io/badge/SQLite-3-blue)](https://www.sqlite.org/docs.html)
# Django Blog App

This is a Django-based blog application that allows users to create, read, update, and delete blog posts. It also includes features such as categorization, tagging, user authentication, and contact form submission.

## Acknowledgements

The project was inspired by various open-source Django projects and tutorials available online.

## API Reference

This project does not include an API. It is a monolithic web application built with Django.

## Appendix

The project includes several Django apps and templates. The main app is `djangoapp`, which contains the core functionality for the blog application.

## Authors

- [Mohammed Kaif](https://github.com/MohammedKaif037)

## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

## Color Reference

The project uses the following color palette:

| Color             | Hex                                                        |
| ----------------- | ---------------------------------------------------------- |
| Primary Color     | ![#006769](https://via.placeholder.com/10/000000?text=+) `#006769` |
| Secondary Color   | ![#40A578](https://via.placeholder.com/10/FFFFFF?text=+) `#40A578` |
| Accent Color      | ![#00FF00](https://via.placeholder.com/10/00FF00?text=+) `#00FF00` |

## Contributing

Contributions are welcome! Please follow the standard GitHub workflow for contributing to open-source projects.

## Installation

To install and run the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/MohammedKaif037/django-blog-app.git
    ```

2. Navigate to the project directory:
    ```bash
    cd django-blog-app
    ```

3. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use env\Scripts\activate
    ```

4. Install the required dependencies:
    ```bash
    pip install django
    ```

5. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

7. Open your web browser and visit `http://localhost:8000` to access the application.

## Deployment

The project can be deployed to various hosting platforms, such as:

- Heroku
- AWS (Elastic Beanstalk, EC2)
- DigitalOcean
- Azure

Refer to the respective platform's documentation for deployment instructions.
**Q: How do I customize the blog appearance?**

A: The project uses Bootstrap for styling. You can modify the CSS files in the `static/css` directory to customize the appearance.

## Features

- User authentication (registration, login, logout)
- CRUD operations for blog posts
- Categorization and tagging of blog posts
- Featured posts section
- Contact form submission
- Search functionality
- Pagination for post listings
## Feedback

If you have any feedback or suggestions for improvement, please open an issue on the project's GitHub repository.
## Screenshots

### Screenshot 1 - HOME
![Screenshot 1](https://github.com/MohammedKaif037/DjangoBlog/blob/main/Screenshots/bloghome.png)

### Screenshot 2 - BlogPost
![Screenshot 2](https://github.com/MohammedKaif037/DjangoBlog/blob/main/Screenshots/blogpost.png)

### Screenshot 3 - Category
![Screenshot 3](https://github.com/MohammedKaif037/DjangoBlog/blob/main/Screenshots/category.png)

### Screenshot 4 - Tag
![Screenshot 4](https://github.com/MohammedKaif037/DjangoBlog/blob/main/Screenshots/tag.png)

### Screenshot 5 - Contact
![Screenshot 5](https://github.com/MohammedKaif037/DjangoBlog/blob/main/Screenshots/contactblog.png)

## Style Guide

The project follows the [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/) for Python code and the [Bootstrap documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/) for HTML/CSS/JS.
## Support

If you encounter any issues or have questions about the project, please open an issue on the project's GitHub repository or reach out to the project maintainers.

























