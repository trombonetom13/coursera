import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup as beso
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
position = int(input("Enter position:"))-1
count = int(input("Enter count:"))
html = urllib.request.urlopen(url, context=ctx).read()
soup = beso(html, 'html.parser')
sequence = []
tags = soup('a')
for i in range(count):
    link = tags[position].get('href', None)
    print("Retrieving:",link)
    sequence.append(tags[position].contents[0])
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = beso(html, 'html.parser')
    tags = soup('a')
    link = tags[position].get('href', None)
print(sequence[-1])
