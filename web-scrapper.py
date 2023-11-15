import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://books.toscrape.com"
result = requests.get(url)
soup = BeautifulSoup(result.content, 'html.parser')
articles = soup.find_all('article')


for article in articles:
    titles = article.h3.a["title"]
    ratings = article.p["class"][1]
    print (titles, ratings)
