import telebot
import random

# Вставь сюда свой токен от BotFather
TOKEN = '8621599669:AAFG-Ac-wqF9prAD3KgL-0rjUxB2OvNVEck'

bot = telebot.TeleBot(TOKEN)

# Список случайных ответов
RESPONSES = [
    "Ха! Интересно! 😄",
    "Ты прав! 👍",
    "Ты не прав! 👎",
    "Это просто гениально! 🧠",
    "Мм, может быть... 🤔",
    "Конечно! ✅",
    "Никогда! ❌",
    "Расскажи мне больше! 📖",
    "Лол! 😂",
    "Вот это да! 🚀",
    "Согласен на 100%! 💯",
    "Не знаю что сказать... 😶",
    "Это шедевр! 🎨",
    "Скучно... 😑",
    "Офигеть! 🤯",
]

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет! 👋\nЯ тестовый бот, отвечаю на всё! 🤖\nНапиши мне что-нибудь!')

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, '/start - Начать\n/help - Помощь\n\nИли просто напиши что-нибудь!')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    response = random.choice(RESPONSES)
    bot.reply_to(message, response)

if __name__ == '__main__':
    print("🤖 Бот запущен! Жди сообщений...")
    bot.infinity_polling()
