#                                       Django Internship Assignment 


A Django REST Framework project demonstrating backend development skills including API Authentication, Celery Background Tasks, Telegram Bot Integration.


## Tech Stack

- **Django**
- **Django RESt Framework**
- **PostGreSQL**
- **Celery**
- **Telegram Bot API**
- **JWT**


---


## Features

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


---


# Link to API Documentation - 
[Postman Collection Link](https://documenter.getpostman.com/view/37031551/2sB2x8ErFC)


---



##   Set up to run the project


1.Create Virtual Environment
-    python -m venv myenv
-    On Linux/Mac : source venv/bin/activate  
-    On Windows: myenv\Scripts\activate

2.Install Requiremnets
-    pip install -r requirements.txt

3.Setup .env file ( in root directory)
-    /projectname/.env

```env

DEBUG=False
SECRET_KEY=your-secret-key
EMAIL_BACKEND = django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST = smtp.gmail.com
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER =youremail@example.com
EMAIL_HOST_PASSWORD=your-email-password-here
TELEGRAM_BOT_TOKEN=your-telegram-bot-token-here

```


4.Apply Migrations
-    python manage.py migrate

5.create SuperUser
-    python manage.py createsuperuser

6.Run the Server
-    python manage.py runserver


7. Start Celery Worker  
-   celery -A Internship worker -l info --pool=solo  


   ![Celery Mail](https://raw.githubusercontent.com/sugandhi15/Internship_Assignment/main/Assets/CeleryMail.jpeg)



8. Start Telegram bot  
-   python manage.py telegram_bot  


   ![Telegram Bot Working](https://raw.githubusercontent.com/sugandhi15/Internship_Assignment/main/Assets/Telegram_Bot.png)




    
