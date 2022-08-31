import requests
from bs4 import BeautifulSoup

"""
A simple data scraping script to get a data science books list from pdf drive. 
"""

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 "
                         "Safari/537.36"}
# I used pdfdrive to get book names.
response = requests.get("https://www.pdfdrive.com/data-science-books.html", headers=headers)
webpage = response.content

soup = BeautifulSoup(webpage, "html.parser")
books = {}

# If you used a different website to get book names, you may need different tags.
for parent in soup.find_all("ul"):
    for n, tag in enumerate(parent.find_all("li")):
        title = [x for x in tag.find_all(class_="ai-search")]
        for item in title:
            books[item.text.strip()] = 0
print(books)
