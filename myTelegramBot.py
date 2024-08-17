import telebot
from telebot import util
from g4f.client import Client
from parserYandexWeather import getWeatherFromSity,getInfoWithComma

client = Client()
openFile = (open('D:/token.txt','r'))

token = (openFile.readline())
bot = telebot.TeleBot(token, parse_mode=None)
openFile.close()

@bot.message_handler(commands=['weather'])
def getWeather(message):
    urlKirov = "https://yandex.ru/weather/ru-RU/details/gardening/today?lat=58.5953598&lon=49.59811401&lang=ru&via=ms"
    weatherDataFromParser = str(getWeatherFromSity(urlKirov))

    questionToGpt = f"Напиши рекомендации, как одеться для мужчины и женщины для утренней, дневной, вечерней и ночной прогулки на основе этих данных погоды:\n"+weatherDataFromParser

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": questionToGpt}]
    )
    weatheransv = str(response.choices[0].message.content)

    bot.reply_to(message,util.smart_split(weatheransv,chars_per_string=3000))

@bot.message_handler(func=lambda message: True)
def echo_all(userMessage):   
	response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": userMessage}]
    )
	gptAnswer = str(response.choices[0].message.content)
	bot.reply_to(userMessage,util.smart_split(gptAnswer,chars_per_string=3000) )
	
bot.infinity_polling()
