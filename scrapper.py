import requests
from bs4 import BeautifulSoup
import pandas as pd

quotes = []
authors = []

# Loop through pages
for page in range(1, 6):
    url = f"http://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for quote in soup.find_all("span", class_="text"):
        quotes.append(quote.text)

    for author in soup.find_all("small", class_="author"):
        authors.append(author.text)

# Save data
data = pd.DataFrame({
    "Quote": quotes,
    "Author": authors
})

data.to_csv("quotes_multiple_pages.csv", index=False)

print("✅ Multi-page scraping complete!")
