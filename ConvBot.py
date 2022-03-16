import telebot
from config import TOKEN, cur
from Token_bot import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start", "help"])
def start(message: telebot.types.Message):
    text = "Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты> \
    <в какую валюту перевести> \
    <количество конвертируемой валюты> Увидеть список всех доступных валют - /values"
    bot.reply_to(message, text)


@bot.message_handler(commands=["values"])
def values(message: telebot.types.Message):
    text = "Доступны следующие валюты: "
    for key in cur:
        text = "\n".join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=["text"])
def conv(message: telebot.types.Message):
    try:
        values = message.text.split(" ")
        if len(values) != 3:
            raise ConvException("Проверьте введенные данные")
        first, second, summ = values
        parsing = Converter.convert(first, second, summ)
    except ConvException as e:
        bot.reply_to(message, f"Ошибка пользователя \n{e}")

    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать валюту\n{e}")
    else:
        text = f"Цена {summ} {first} равна {parsing} {second}"
        bot.send_message(message.chat.id, text)


bot.polling(non_stop=True)
