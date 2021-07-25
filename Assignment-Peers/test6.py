import urllib.request,urllib.parse,urllib.error
import json

# url= http://py4e-data.dr-chuck.net/comments_1252043.json
sum,count=0,0
url=input('Enter location:')
print('Retrieving',url)
uh=urllib.request.urlopen(url)
data=uh.read().decode()
print('Retrieved',len(data),'characters')
info=json.loads(data)

sum=0
count=0
for item in info['comments']:
    sum+=item['count']
    count+=1

print('Count:',count)
print('Sum:',sum)
