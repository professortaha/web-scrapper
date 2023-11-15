import requests
from bs4 import BeautifulSoup

def get_book_data(book):
    title = book.h3.a["title"]
    rating = book.select_one('p[class^="star-rating"]')['class'][1]
    return {'title': title, 'rating': rating}

def scrape_books(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article')
        return [get_book_data(article) for article in articles]
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []

# Main code
url = "https://books.toscrape.com"
book_data_list = scrape_books(url)

# Print the titles and ratings
print("Book Titles and Ratings:")
for data in book_data_list:
    print(f"Title: {data['title']}, Rating: {data['rating']}")
