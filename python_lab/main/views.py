from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
from django.conf import settings

def index(request):
    appid = settings.APPID
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name']
            existing_city = City.objects.filter(name=city_name).exists()
            if not existing_city:
                res = requests.get(url.format(city_name)).json()
                if res['cod'] == 200:
                    form.save()
                else:
                    form.add_error('name', 'Місто не знайдено')
            else:
                form.add_error('name', 'Місто вже додане')
    else:
        form = CityForm()

    all_cities = []
    cities = City.objects.all()
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'humidity': res["main"]["humidity"],
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }
        all_cities.append(city_info)

    data = {
        'title': 'Main page?',
        'all_info': all_cities,
        'form': form,
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')
