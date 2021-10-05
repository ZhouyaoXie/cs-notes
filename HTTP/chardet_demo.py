import urllib.request
import chardet
from chardet.universaldetector import UniversalDetector

url = 'http://www.cs.cmu.edu/~ehn/'
with urllib.request.urlopen(url) as response:
	print(chardet.detect(response.read()))

det = UniversalDetector()
url2 = 'https://www.cs.cmu.edu/~pausch/Randy/Randy/Randy_medical_Chinese_2007/shortsummary_C.html'
with urllib.request.urlopen(url2) as response:
	for line in response.readlines():
		det.feed(line)
		if det.done: break

det.close()
print(det.result)

