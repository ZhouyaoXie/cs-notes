from bs4 import BeautifulSoup
import requests

url = 'http://api.lyrics.ovh/v1/Ed Sheeran/Thinking out Loud'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser') # resp.text in str, resp.content in bytes
# get return HTML string
soup.text

# find
res = soup.find('a')
print(res.text.strip()) 
print(res.attrs) # a dictionary

# find_all
line = []
for head in soup.find_all('h1'):
	for s in head.find_all('p'):
		line.append(s.text.strip())	

# find by regular expressions
import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)

# find by keyword arguments
soup.find_all(id='link1', href='http://')
soup.find_all(attrs={'name': 'email', 'data-foo': 'value'})

# find by CSS class
soup.find_all("a", class_="title")
soup.select('body div ul li.c-author-list__item')
