
from django.shortcuts import render, redirect
from weather_api.key import api_key  # Assuming you have a key.py file with your API key
import requests
import math

def index(request):
    return render(request, "weather_api/home.html")

def result(request):
    if request.method == "POST":
        city_name = request.POST["city"].lower()
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"
        try:
            w_dataset = requests.get(url).json()
            context = {
                "city_name": w_dataset["city"]["name"],
                "city_country": w_dataset["city"]["country"],
                "wind": w_dataset['list'][0]['wind']['speed'],
                "degree": w_dataset['list'][0]['wind']['deg'],
                "status": w_dataset['list'][0]['weather'][0]['description'],
                "cloud": w_dataset['list'][0]['clouds']['all'],
                'date': w_dataset['list'][0]["dt_txt"],
                'date1': w_dataset['list'][1]["dt_txt"],
                'date2': w_dataset['list'][2]["dt_txt"],
                'date3': w_dataset['list'][3]["dt_txt"],
                'date4': w_dataset['list'][4]["dt_txt"],
                'date5': w_dataset['list'][5]["dt_txt"],
                'date6': w_dataset['list'][6]["dt_txt"],
                "temp": round(w_dataset["list"][0]["main"]["temp"] - 273.0),
                "temp_min1": math.floor(w_dataset["list"][1]["main"]["temp_min"] - 273.0),
                "temp_max1": math.ceil(w_dataset["list"][1]["main"]["temp_max"] - 273.0),
                "temp_min2": math.floor(w_dataset["list"][2]["main"]["temp_min"] - 273.0),
                "temp_max2": math.ceil(w_dataset["list"][2]["main"]["temp_max"] - 273.0),
                "temp_min3": math.floor(w_dataset["list"][3]["main"]["temp_min"] - 273.0),
                "temp_max3": math.ceil(w_dataset["list"][3]["main"]["temp_max"] - 273.0),
                "temp_min4": math.floor(w_dataset["list"][4]["main"]["temp_min"] - 273.0),
                "temp_max4": math.ceil(w_dataset["list"][4]["main"]["temp_max"] - 273.0),
                "temp_min5": math.floor(w_dataset["list"][5]["main"]["temp_min"] - 273.0),
                "temp_max5": math.ceil(w_dataset["list"][5]["main"]["temp_max"] - 273.0),
                "temp_min6": math.floor(w_dataset["list"][6]["main"]["temp_min"] - 273.0),
                "temp_max6": math.ceil(w_dataset["list"][6]["main"]["temp_max"] - 273.0),
                "pressure": w_dataset["list"][0]["main"]["pressure"],
                "humidity": w_dataset["list"][0]["main"]["humidity"],
                "sea_level": w_dataset["list"][0]["main"]["sea_level"],
                "weather": w_dataset["list"][1]["weather"][0]["main"],
                "description": w_dataset["list"][1]["weather"][0]["description"],
                "icon": w_dataset["list"][0]["weather"][0]["icon"],
                "icon1": w_dataset["list"][1]["weather"][0]["icon"],
                "icon2": w_dataset["list"][2]["weather"][0]["icon"],
                "icon3": w_dataset["list"][3]["weather"][0]["icon"],
                "icon4": w_dataset["list"][4]["weather"][0]["icon"],
                "icon5": w_dataset["list"][5]["weather"][0]["icon"],
                "icon6": w_dataset["list"][6]["weather"][0]["icon"],
            }
        except Exception as e: # Catching all exceptions is generally not recommended, but is used here for simplicity.
            print(f"Error: {e}") #Good for debugging
            context = {
                "city_name": "Not Found, Check your spelling...",
            }

        return render(request, "weather_api/results.html", context)
    else:
        return redirect('home')

def about(request):
    return render(request, 'weather_api/about.html')

def contact(request):
    return render(request, 'weather_api/contact.html')

# weather_api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('result/', views.result, name='result'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]

# weather_api/key.py
# Place your API key here
api_key = "YOUR_OPENWEATHERMAP_API_KEY" #replace with your key.

# weather_api/templates/weather_api/home.html (Example)
# Add your html here.
# weather_api/templates/weather_api/results.html (Example)
# Add your html here.
# weather_api/templates/weather_api/about.html (Example)
# Add your about html here.
# weather_api/templates/weather_api/contact.html (Example)
# Add your contact html here.

# WeatherBug/urls.py (Example. add this to the list of url patterns)
from django.urls import include, path

urlpatterns = [
    # ... your other URL patterns ...
    path('', include('weather_api.urls')),
]