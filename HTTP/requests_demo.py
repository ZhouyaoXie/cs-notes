import requests

# GET
url = 'http://api.lyrics.ovh/v1/Ed Sheeran/Thinking out Loud'
response = requests.get(url)
if response.status_code == 404:
	print('No lyrics found.')
if response.status_code == 200:
	print(response.text)

# POST
import json 
url = 'https://sentim-api.herokuapp.com/api/v1/'
headers = {'Content-Type': 'application/json'}
new_data = {'text': 'this is a happy post!'}
response = requests.post(url, headers = headers, data = json.dumps(new_data))
print(response.status_code)
print(json.loads(response.text)) # or, response.json()

# PUT PATCH
# no headers

# DELETE
# response returns empty JSON objet
