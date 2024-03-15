from flask import Flask, jsonify
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

# Replace API_KEY with your actual API key from OpenWeatherMap
API_KEY = 'c7e64467335583b65299987b991c76c4'


def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data


@app.route('/weather', methods=['GET'])
def weather_forecast():
    cities = ['Manila', 'Taguig', 'Makati', 'Paranaque', 'Pasig']
    weather_data = {}

    for i, city in enumerate(cities):
        today = datetime.now().date()
        forecast_date = today - timedelta(days=i)
        if i == 0:
            forecast_info = "Today’s Weather Forecast Details"
        elif i == 1:
            forecast_info = "Tomorrow’s Weather Forecast Details"
        elif i == 2:
            forecast_info = "Yesterday’s Weather Forecast Details"
        elif i == 3:
            forecast_info = "Next Monday Weather Forecast Details"
            forecast_date += timedelta((0 - forecast_date.weekday() + 7) % 7)
        else:
            forecast_info = "Next Month Weather Forecast Details"
            forecast_date += timedelta(days=30)

        weather_data[city] = {
            "Forecast Details": forecast_info,
            "Date": forecast_date.strftime("%Y-%m-%d"),
            "Weather": get_weather(city),
            "Country": "Philippines",
            "City": city
        }

    return jsonify(weather_data)


if __name__ == '__main__':
    app.run(debug=True)
