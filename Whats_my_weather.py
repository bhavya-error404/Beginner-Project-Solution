import requests
import time

city = input("Enter your City: ")
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=dcd4b9138af29a884fb48ee90410521f&units=imperial'.format(city)
res = requests.get(url)
data = res.json()
weathe = data['weather'][0]['main']
max_temp = data['main']['temp_max']
min_temp = data['main']['temp_min']

print("Weather is:",weathe)
print("Maximum Temperature is :",max_temp)
print("Minimum Temperature is :",min_temp)

time.sleep(2)
