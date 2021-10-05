[Reference 1](https://www.interviewbit.com/rest-api-interview-questions/#rest-api-basic-interview-questions)

[Reference 2](https://www.softwaretestinghelp.com/restful-web-services-interview-question/)

## REST

REST stands for Representational State Transfer and uses HTTP protocol for implementation. 

#### RESTful Web Services

Properties: 

- It is based on the stateless client-server architecture.
  - stateless: the client state is not maintained on the server.
- It provides maintainability and scalability.
- It uses HTTP protocol.
- Resources are accessible to the service through URIs.
- It defines methods of accessing resources at server required for the client by means of request headers, request body, response body, status code, etc.
- It supports caching.

Disadvantages:

- Stateless: it is not possible to maintain sessions. Session simulation relies on the client-side to pass the session id.
- REST does not impose security restrictions inherently.

#### REST Resource
 
Every content in the REST architecture is considered a resource. The REST server provides access to these resources whereas the REST client consumer these resources. Every resource is identified globally via a URI.

#### URI

Uniform Resource Identifier is used for identifying each resource of the REST architecture.
- URN: Uniform Resource Name identifies the resource via a name, e.g. isbn. URN doesn't always specify where to locate the resource on the internet.
- URL: Uniform Resource Location allows one to fetch the resource from its location.
  
#### Messaging
  
Messaging is the medium of communication between the client and the server. Sending a message from the REST client to the REST server in the form of an HTTP request, and the server responding back with an HTTP response.
  
#### Differences between SOAP and REST
  
- SOAP is a protocol, while REST is an architectural design pattern for developing web services.
- SOAP can not use REST as its protocol, but REST architecture can have SOAP protocol as part of the implementation.
- SOAP is more rigid in the sense that its standards must be followed strictly, while REST defines standards but they need not be strictly followed.
- SOAP defines its own security measures, while REST only inherits the security measure based on what protocol it uses for the implementation. 

#### Idempotent methods

Even after calling a single request multiple times, the outcome of the requests should be the same.
- POST is not idempotent. GET, OPTIONS, TRACE, PUT, HEAD, DELETE are idempotent methods.

## HTTP

#### HTTP Methods

- GET
- POST: create new resources on the server
- PUT: update existing resource on the server or to replace the resource
- DELETE
- PATCH: modify the resource on the server.
- OPTIONS
  
#### HTTP Status Codes
  
- 400 - Bad Request - client side failed input validation
- 401 - unauthorized - user is not authenticated
- 403 - Forbidden - user is authenticated but not authorized to access the resource


#### HTTP Request

- Method
- URI
- HTTP Version
- Request header
- Request body

#### HTTP Response

- HTTP Version
- Response code
- Response header
- Response body

#### Payload

The request data which is rpesent in the body of every HTTP message. In RESTful web service, the payload can only be passed to the recipient through the POST method.'

## urllib

[urllib tutorial](https://docs.python.org/3/howto/urllib2.html#urllib-howto)

[urllib.parse documentation](https://docs.python.org/3/library/urllib.parse.html)

#### Read from a url
```
import urllib.request

with urllib.request.urlopen('http://python.org') as response:
	html = response.read() # bytes
	print(response.url)
	print(response.headers)
	print(response.status)
```
```
req = urllib.request.Request('http://www.voidspace.org.uk')
with urllib.request.urlopen(req) as response:
	the_page = response.read()
```

#### POST request, send in data

```
import urllib.parse
url = 'https://pastebin.com/api/api_post.php'
values = {'api_paste_code': 'random text to paste',
			'api_paste_name': 'title.py',
			'api_paste_format': 'py'}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
	the_page = response.read()
  ```

#### GET request, encode data in the url itself

```
url_values = urllib.parse.urlencode(data)
full_url = rul + '?' + url_values
html = urllib.request.urlopen(full_url)
```

#### Pass in headers
```
headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(url, data, headers)
html = urllib.request.urlopen(full_url)
```

### Exceptions

#### URLError
Could not reach the server due to no network connection.

#### HTTPError
The server could not fulfil the request.

```
try:
	urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
	print(e.code)
	print(e.read())
except urllib.error.URLError as e:
	print(e.reason)
```

### URL Parsing
```
import urllib.parse
o = urllib.parse.urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')
print(o.scheme, 
	o.port, 
	o.path, 
	o.netloc, 
	o.params, 
	o.query, 
	o.geturl())
  ```
