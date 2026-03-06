import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Включаем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Ваш токен бота от BotFather
TOKEN = '8621599669:AAFG-Ac-wqF9prAD3KgL-0rjUxB2OvNVEck'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /start"""
    await update.message.reply_text(
        'Привет! 👋\n'
        'Я тестовый бот, который отвечает на всё что угодно!\n'
        'Напиши мне что-нибудь...'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /help"""
    await update.message.reply_text(
        'Доступные команды:\n'
        '/start - Начать\n'
        '/help - Помощь\n'
        '/echo - Повторить текст\n\n'
        'Или просто напиши мне что-нибудь!'
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /echo"""
    if context.args:
        text = ' '.join(context.args)
        await update.message.reply_text(f'Ты сказал: {text}')
    else:
        await update.message.reply_text('Используй: /echo <текст>')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик всех сообщений"""
    user_message = update.message.text
    
    responses = [
        f'Интересно: {user_message}',
        f'Ты написал: {user_message} 🤔',
        f'Прикольно! "{user_message}"',
        'Согласен! ✅',
        'Не согласен! ❌',
        'Может быть... 🤷',
        f'Ха-ха! {user_message}',
        'Расскажи мне больше!',
        'Это помощь? 🆘',
        f'"{user_message}" - вот это да! 🚀',
    ]
    
    import random
    response = random.choice(responses)
    await update.message.reply_text(response)

async def main() -> None:
    """Запуск бота"""
    # Создаём Application
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчики команд
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('echo', echo))
    
    # Обработчик всех остальных сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запускаем бота
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
