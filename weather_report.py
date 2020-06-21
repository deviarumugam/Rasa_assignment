import requests

def Weather(city_name):
    url='http://api.openweathermap.org/data/2.5/weather?appid=7f8199a5d7850041a748b0fc3bcf471a&q='
    url = url + city_name
    json_weather_data = requests.get(url).json()
    weather_main = json_weather_data['main']
    return weather_main