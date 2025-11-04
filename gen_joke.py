import requests
import json

r = requests.get(url='https://official-joke-api.appspot.com/random_joke')

joke = json.loads(r.text)

print(joke)
