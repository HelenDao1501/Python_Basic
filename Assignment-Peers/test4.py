import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup


url = input('Enter an url:')
if len(url) <1: url = 'http://py4e-data.dr-chuck.net/known_by_Keiryn.html'
count = int(input('Enter count:'))
position = int(input('Enter position:'))

#Retrive all of the anchor tags

for i in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    tag = tags[position-1]
    html = tag.get('href',None)
    url = html
    print('Retrieving:', url)
