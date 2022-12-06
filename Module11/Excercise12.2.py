import urllib.request
import re
from bs4 import BeautifulSoup
import collections
collections.Callable = collection.abc.Callable

html = urlib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1648177.html').read()
soup = BeautifulSoup(html, 'html.parser')

sum=0

tags = soup('span')
for tag in tags:
    y=str(tag)
    x= re.findall('[0-9]+',y)
    for i in x:
        i=int(i)
        sum=sum+i
print(sum)
