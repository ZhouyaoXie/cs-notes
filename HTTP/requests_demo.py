import requests

# # demo 1: GET with requests.get()
url = 'http://api.lyrics.ovh/v1/Ed Sheeran/Thinking out Loud'
response = requests.get(url)
if response.status_code == 404:
	print('No lyrics found.')
if response.status_code == 200:
	print(response.text)

# demo 2: POST with requests.post()
import json 

url = 'https://sentim-api.herokuapp.com/api/v1/'
text = 'this is a happy post!'
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
response = requests.post(url, headers = headers, data = json.dumps({'text': text}))
print(response.status_code)
print(json.loads(response.text)['result'])
