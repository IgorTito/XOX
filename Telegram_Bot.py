import telebot
import requests
import json
from Token import *

bot = telebot.TeleBot(TOKEN)

keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row("Москва", "Санкт-Петербург", "Волгоград")
keyboard.row("Рим", "Дубай", "Токио")
keyboard.row("Лондон", "Париж", "Берлин")
keyboard.row("Пекин", "Нью-Йорк", "Сеул")
@bot.message_handler(commands=["start", "help"])
def start(message: telebot.types.Message):
    start = "Для того, чтобы узнать прогноз погоды, введите /weather или выберите из представленных"
    bot.reply_to(message, start, reply_markup = keyboard)


@bot.message_handler(commands=["weather"])
def weather(message: telebot.types.Message):
    weather = "Для того, чтобы узнать прогноз погоды, введите наименование города или выберете из представленных"
    bot.reply_to(message, weather)


@bot.message_handler(content_types=["text"])
def weather_place(message: telebot.types.Message):
    city = message.text

    answer = requests.get(f"http://api.openweathermap.org/data/2.5/weather?appid={api_key_weather}&q={city}")

    place = json.loads(answer.content)

    try:
        weather = place["main"]
    except KeyError:
        bot.reply_to(message, f"🤔Проверьте правильность написания города - '{city}'\
        , введите название без использования цифр или других символов")
    try:
        temperature = round(weather["temp"] - 273, 1)
        pressure = weather["pressure"] * 0.75
        temp_feels = round(weather["feels_like"] - 273, 1)
        wind = place["wind"]
        speed = wind["speed"]
        description = place["weather"][0]["main"]
        if description == "Rain" or description == "Drizzle":
            description = "\U00002614дождь"
            bot.send_message(message.chat.id, "Возьмите зонтик - на уличе идет дождь!")
        elif description == "Snow":
            description = "\U00002744снегопад"
        elif description == "Clear":
            description = "\U00002600ясно"
        elif description == "Clouds":
            description = "\U00002601облачно"
        elif description == "Mist":
            description = "\U0001F301туман"

        bot.reply_to(message, f"В данный момент температура в городе ~🌇{city}~\
                             \nсоставляет 🌡{temperature} C,\
                             \nощущается как 🌡{temp_feels}\
                             \nатмосферное давление -  ☇{pressure} мм ртутного столба,\
                             \nскорость ветра достигает 🌪{speed} м/сек, \
                             \nсейчас на улице - {description}")
    except:
        pass
    try:
        if temperature <= 10.0:
            bot.send_message(message.chat.id, "Наденьте теплую одежду, на улице холодно🥶")
        elif 10.1 <= temperature <= 29.9:
            bot.send_message(message.chat.id, "На улице - тепло, можете одеться полегче😋")
        elif temperature >= 30.0:
            bot.send_message(message.chat.id, "На улице - жарко, не забудьте головной убор🥵")
    except:
        pass




bot.polling()
