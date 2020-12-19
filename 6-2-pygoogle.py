#!/usr/bin/python3
# Pygoogle.py -> Opens several Google search results
import sys
import requests
import webbrowser
import bs4
print('Googling')                                                           
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1]))
res.raise_for_status()

#Retrive top search result links.
#Open a browser tab for each result.
# Retrive top search result links.

mysoup = bs4.BeautifulSoup(res.text,"html.parser")
# Open a browser tab for each result.
link = mysoup.select('.r a')
numOpen = min(5,len(link))
#
for i in range(numOpen):
    webbrowser.open('http://google.com' +  link[i].get('href'))
