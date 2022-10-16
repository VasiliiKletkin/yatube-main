# YaTube

## Описание
On the site you can post news, post pictures, comment on posts, divide posts into groups (categories), subscribe to your favorite author. Implemented caching, works on the main page and is updated every 20 seconds. Written unit tests. In the admin panel, in addition to the standard set of features, you can delete posts, comments and groups.

The project was created for educational purposes. Stack was used:
Python, Django, Git, Bootstrap, nginx, gunicorn, PostegreSQl,

## Установка 
Clone the repository on the local machine:

```$ git clone https://github.com/vkletkin/yatube-main```

 Create a virtual environment:
 
 ```$ python -m venv venv```
 
 Install dependencies:

```$ pip install -r requirements.txt```

Creating and applying migrations:

```$ python manage.py makemigrations``` и ```$ python manage.py migrate```

Starting the django server:

```$ python manage.py runserver```
