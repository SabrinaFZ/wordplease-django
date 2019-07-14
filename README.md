# Wordplease

A website and API created with Django and Django Rest Framework

## Installation

1. Clone the repository
```
git clone https://github.com/SabrinaFZ/wordplease-django
```

2. Create environment
```
virtualenv env
```

3. Activate environment
```
source env/scripts/activate
```

4. Install requirements
```
pip install -R requirements.txt
```

5. Create Database
```
python manage.py migrate
```

6. Create super user to access admin
```
python manage.py createsuperuser
```

7. Run the server
```
python manage.py runserver
```

## Website

|URL | Description
|------ | ------ |
| /home | Show all the latests posts
| /blogs | Show all blogs
| /blogs/<str:username>/ | Show all the blogs from an user
| /blogs/<str:username>/<int:pk> | Show details of a post from a blog
| /new-post | Create a new post
| /login | Login to the app
| /sign-up | Create a new user
| /logout | Logout from the app

## API

- Go to the [Wordplease API documentation](https://documenter.getpostman.com/view/6434972/SVSHrpkJ?version=latest)


## Author

Sabrina Fernandez Zambrano
