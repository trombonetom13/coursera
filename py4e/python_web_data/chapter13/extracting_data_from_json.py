import urllib.request, urllib.error, urllib.parse
import json

url = input('Enter location:')
print('Retrieving', url)
uh = urllib.request.urlopen(url).read()
print('Retrieved', len(uh), 'characters')

js = json.loads(uh.decode('utf-8'))

res = 0

for comment in js['comments']:
    res = res + comment['count']

print('Sum:', res)
