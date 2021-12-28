import tkinter as tk
import requests
import time
from flask import Flask, request

app = Flask(__name__)

@app.route('/weather', methods=['GET', 'POST'])
def get_weather():
    if request.method == 'POST':
        city = request.form.get('city')
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=e02d7c519c32d7195c0cab0c58850c06"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise']))
        sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset']))

        return '''
                  <h2>The temperature in {} is {}°C</h2>
                  <h2>Min temperature is {}°C and Max temperature is {}°C</h2>'''.format(city, temp, min_temp, max_temp)

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>City: <input type="text" name="city"></label></div>
               <input type="submit" value="Submit">
           </form>'''

if __name__ == '__main__':
   app.run()