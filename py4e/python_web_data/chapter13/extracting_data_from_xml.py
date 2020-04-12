import urllib.request as ur
import xml.etree.ElementTree as et

url = input('Enter location: ')

total = 0
sum = 0

print('Retrieving', url)
xml = ur.urlopen(url).read()
print('Retrieved', len(xml), 'characters')

tree = et.fromstring(xml)
counts = tree.findall('.//count')
for count in counts:
    sum += int(count.text)
    total += 1

print('Count:', total)
print('Sum:', sum)
