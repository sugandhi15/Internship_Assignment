#                                       Django Internship Assignment 


A Django REST Framework project demonstrating backend development skills including API Authentication, Celery Background Tasks, Telegram Bot Integration.


## Tech Stack

- **Django**
- **Django REST Framework**
- **PostGreSQL**
- **Celery**
- **Telegram Bot API**
- **JWT**


---


## Features

1. API Endpoints
    Public : can be accessed by anyone.
    Protected : needs token or JWT.

2. Celery 
    Handles background tasks or long-running operations. 
    Background task: Send email after user registration.

3. Telegram Bot
    Allows user to interact with our Django application through Telegram.
    A Telegram bot that listens to `/start`.
    Stores the Telegram username into the database.


---



##   Set up to run the project


1.Create Virtual Environment
-    python -m venv myenv
-    On Linux/Mac : source venv/bin/activate  
-    On Windows: myenv\Scripts\activate

2.Install Requirements
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

5.Create SuperUser
-    python manage.py createsuperuser

6.Run the Server
-    python manage.py runserver

7.Start Celery Worker  
-   celery -A Internship worker -l info --pool=solo  

8.Start Telegram bot  
-   python manage.py telegram_bot  

---


# Link to API Documentation - 

[Postman Collection Link](https://documenter.getpostman.com/view/37031551/2sB2x8ErFC)


---


## Celery Task – Email Confirmation

   ![Celery Mail](https://raw.githubusercontent.com/sugandhi15/Internship_Assignment/main/Assets/CeleryMail.jpeg)


---

## Telegram Bot – Screenshot


   ![Telegram Bot Working](https://raw.githubusercontent.com/sugandhi15/Internship_Assignment/main/Assets/Telegram_Bot.png)


---


## Contact

If you have any questions or suggestions, feel free to reach out:

- GitHub: [sugandhi15](https://github.com/sugandhi15)
- Email: sugandhibansal26@gmail.com

Thanks for checking out the project!