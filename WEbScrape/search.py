from googlesearch import search
import urllib.request
from bs4 import BeautifulSoup

def google_scrape(url):
    thepage = urllib.request.urlopen(url)
    soup = BeautifulSoup(thepage, "html.parser")
    return soup.title.text

i = 1
query = 'Nightcore Metry'
for url in search(query):
    a = google_scrape(url)
    print (str(i) + ". " + a)
    print (url)
    print (" ")
    i += 1