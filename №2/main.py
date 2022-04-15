import json
import requests

response = requests.get("https://api.weatherbit.io/v2.0/current?key=0dfc25d435314774a46211f8cdf5900f&city_id=8953360").text
response_info = json.loads(response)
print('В городе', (response_info['city_name']), 'сейчас', (response_info['temp']), 'градусов')

