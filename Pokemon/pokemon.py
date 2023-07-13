import requests
 
# Using the example query "demon".
url = "https://api.consumet.org/manga/mangakakalot/demon"
response = requests.get(url)
data = response.json()
print("==========Manga========")
for item in data['results']:
    print("Manga Name : ",item['title'] )
 