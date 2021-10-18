import urllib.request
import urllib.parse
import ssl

# demo for GET request with header
import urllib
import requests
import json

url = 'http://dummy.restapiexample.com/api/v1/employees'
header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
req = urllib.request.Request(url, headers = header)
with urllib.request.urlopen(req) as resp:
	file = resp.read()
data = json.loads(file)
print(type(data)) # dict
print(data['data'])


# demo for POST request
url = 'https://nature.com/'
values = {'q':'music', 'journal':'nature', 'order':'relevance'}
# encode values to data
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
# request values from url
req = urllib.request.Request(url, data)
# open the HTML document
ssl_context = ssl.SSLContext()
ssl_context.load_default_certs()
resp = urllib.request.urlopen(req, context = ssl_context)
# read the first three lines of the document
print(resp.readline())
print(resp.readline())
print(resp.readline())


# example of urllib.parse.urlparse
o = urllib.parse.urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')
print(o.scheme, 
	o.port, 
	o.path, 
	o.netloc, 
	o.geturl())
