import requests
from pprint import pprint
from datetime import datetime

city = input('City: ')

def weather_info(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d5bb44d0fa8e39e2339c9019d833d826&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def weather_discription(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d5bb44d0fa8e39e2339c9019d833d826&units=metric"
    response = requests.get(url)
    data = response.json()
    city_discription = data["weather"][0]

    if city_discription["main"] == "Smoke":
        city_discription_main = f"\U0001f324 {city_discription['main']}"

    elif city_discription["main"] == "Clouds":
        city_discription_main = f"\U0001f325 {city_discription['main']}"

    elif city_discription["main"] == "Clear":
        city_discription_main = f"\U00002600 {city_discription['main']}"

    elif city_discription["main"] == "Tornado":
        city_discription_main = f"\U0001f32a {city_discription['main']}"

    elif city_discription["main"] == "Dust":
        city_discription_main = f"\U0001f300 {city_discription['main']}"

    elif city_discription["main"] == "Sand":
        city_discription_main = f"\U0001f300 {city_discription['main']}"

    elif city_discription["main"] == "Fog":
        city_discription_main = f"\U0001f32b {city_discription['main']}"

    elif city_discription["main"] == "Haze":
        city_discription_main = f"\U0001f32b {city_discription['main']}"

    elif city_discription["main"] == "Mist":
        city_discription_main = f"\U0001f32b  {city_discription['main']}"

    elif city_discription["main"] == "Snow":
        city_discription_main = f"\U000026c4 {city_discription['main']} Можно идти делать снеговика "

    elif city_discription["main"] == "Rain":
        city_discription_main = f"\U0001f327 {city_discription['main']}"

    elif city_discription["main"] == "Drizzle":
        city_discription_main = f"\U0001f326 {city_discription['main']}"

    elif city_discription["main"] == "Thunderstorm":
        city_discription_main = f"\U0001f329 {city_discription['main']}"

    else:
        city_discription_main = city_discription["main"]
    
    information = f"""
    Описание погоды: {city_discription_main }
    
    """
    return information

def weather_fin(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d5bb44d0fa8e39e2339c9019d833d826&units=metric"
    response = requests.get(url)
    data = response.json()
    city_name = {data["name"]}
    city_temp = {data["main"]['temp']}
    city_feels_like = {data["main"]['feels_like']}
    city_humidity = {data["main"]['humidity']}
    city_pressure = {data["main"]['pressure']}
    city_wind = {data['wind']['speed']}
    city_sunset = datetime.fromtimestamp(data["sys"]['sunset'])
    city_sunrise = datetime.fromtimestamp(data["sys"]['sunrise'])
    city_lingth_of_the_day = datetime.fromtimestamp(data["sys"]['sunset']) - datetime.fromtimestamp(data["sys"]['sunrise'])

    information_weather = f"""
    Погода в городе: {city_name}
    Температура: \U0001f321 {city_temp}C
    Ощушается: \U0001f321 {city_feels_like}C
    Влажность: \U0001f302{city_humidity}%
    Давление воздуха: \U0001F32C {city_pressure} гПа
    Ветер: \U0001f32c {city_wind} м/с
    Восход солнца: \U0001f305 {city_sunrise}
    Продолжительность дня: \U0001f305 {city_lingth_of_the_day} \U0001f304
    Закат солнца: \U0001f304 {city_sunset}
    {weather_discription(city)}

    Автор 
        Инстграм - alibek_sh_
        Телеграм - Ali_Shakiro
        Githab - alibekshak
    """
    return information_weather
print(weather_fin(city))