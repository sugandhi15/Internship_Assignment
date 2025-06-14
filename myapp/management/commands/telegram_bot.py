from django.core.management.base import BaseCommand
from telegram.ext import Updater, CommandHandler
from myapp.models import TelegramUser

TELEGRAM_BOT_TOKEN = '7931603576:AAGnnoa1SNeW1B7Z3EAwSy6wT62Dj4oHi-8'

def start(update, context):
    user = update.message.from_user
    TelegramUser.objects.get_or_create(
        telegram_id=user.id,
        defaults={
            'username': user.username or f"user_{user.id}",
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
    )
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome! You've been registered.")

class Command(BaseCommand):
    help = 'Run the Telegram bot'

    def handle(self, *args, **options):
        updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler("start", start))

        self.stdout.write("Bot is running...")
        updater.start_polling()
        updater.idle()