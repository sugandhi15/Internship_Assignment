#####                                        Django Internship Assignment 


A Django REST Framework project demonstrating backend development skills including API Authentication, Celery Background Tasks, Telegram Bot Integration.


# Tech Stack

- Django
- Django RESt Framework
- PostGreSQL
- Celery
- Telegram Bot API
- JWT


# Features

    1. API Endpoints
        Public : can be accesed by anyone.
        Protected : needs token or JWT.

    2. Celery 
        Handles background tasks or long-running operations. 
        Background task: Send email after user registration.

    3. Telegram Bot
        Allows user to interact with our Django application through Telegram.
        A Telegram bot that listens to `/start`.
        Stores the Telegram username into the database.




#   Set up to run the project

    1.Create Virtual Environment
        python -m venv myenv
        On Linux/Mac : source venv/bin/activate  
        On Windows: myenv\Scripts\activate

    2.Install Requiremnets
        pip install -r requirements.txt

    3.Setup .env file ( in root directory)
        /projectname/.env

            DEBUG=False
            SECRET_KEY=django-insecure-0bd01^i&xor+v&d9uwh0*3ye9__p$c7(s-02nh0#8x$$graub2
            EMAIL_BACKEND = django.core.mail.backends.smtp.EmailBackend
            EMAIL_HOST = smtp.gmail.com
            EMAIL_PORT = 587
            EMAIL_USE_TLS = True
            EMAIL_HOST_USER = sugandhibansal26@gmail.com
            EMAIL_HOST_PASSWORD=bfhu tvdh mfzu slxc
            TELEGRAM_BOT_TOKEN=7931603576:AAGnnoa1SNeW1B7Z3EAwSy6wT62Dj4oHi-8

    4.Apply Migrations
        python manage.py migrate

    5.create SuperUser
        python manage.py createsuperuser

    6.Run the Server
        python manage.py runserver

    7.Start Celery Worker
        celery -A Internship worker -l info --pool=solo

        ![Celery Mail](https://github.com/sugandhi15/Internship_Assignment/blob/main/Assets/CeleryMail.jpeg)

    8.Start Telegram bot
        python manage.py telegram_bot

        ![Telegram Bot Working](https://github.com/sugandhi15/Internship_Assignment/blob/main/Assets/Telegram_Bot.png)