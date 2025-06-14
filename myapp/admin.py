from django.contrib import admin
from .models import User, TelegramUser

# Register your models here.
admin.site.register(User)
admin.site.register(TelegramUser)