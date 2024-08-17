import requests
from bs4 import BeautifulSoup

def getInfoWithComma(weatherInfoAll):
    weatherInfo = []
    for i in weatherInfoAll:
        if "," in i:
            weatherInfo.append(i)
        else:
            continue
    return weatherInfo

def getWeatherFromSity(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    hidden_divs = soup.find_all('div', style=lambda value: value and 'clip' in value)

    weatherInfoAll = [div.get_text() for div in hidden_divs]

    weatherInfo = getInfoWithComma(weatherInfoAll)

    return weatherInfo

# print(getWeatherFromSity("https://yandex.ru/weather/ru-RU/details/gardening/today?lat=58.5953598&lon=49.59811401&lang=ru&via=ms"))


