import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://books.toscrape.com"
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract book titles and ratings
    book_data = []
    for book in soup.select('h3 a'):
        title = book.text.strip()
        rating = book.find_previous('p', class_='star-rating')['class'][1]
        book_data.append({'title': title, 'rating': rating})

    # Print the titles and ratings
    print("Book Titles and Ratings:")
    for data in book_data:
        print(f"Title: {data['title']}, Rating: {data['rating']}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
