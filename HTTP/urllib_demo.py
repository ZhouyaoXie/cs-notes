import urllib.request
import urllib.parse
import ssl

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
