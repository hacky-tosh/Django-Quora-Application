# TransportSimple-Quora-Application

## Features

- User registration and authentication system.
- Post questions and answers with rich text content.
- Like/dislike answers.
- User profiles with profile pictures.
- Pagination for question lists.
- Access control: Only authenticated users can answer questions.


## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/django-quora.git
```
2. Create a virtual environment and activate it:
```bash
cd django-quora
python -m venv venv
venv\Scripts\activate #For Windows
```
3. Install the required packages:
```bash
pip install -r requirements.txt
```
4. Apply the database migrations:
```bash
python manage.py migrate
```
5. python manage.py migrate
```bash
python manage.py runserver
```

6.Access the application in your web browser at http://localhost:8000/


##Technologies Used
Django
Django Crispy Forms
Bootstrap 5
SQLite (default database for development)

