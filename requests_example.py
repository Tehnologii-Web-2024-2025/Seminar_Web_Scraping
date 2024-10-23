import requests
from bs4 import BeautifulSoup
import lxml
# url = 'https://www.youtube.com'

# req = requests.get(url)

# print(req.status_code)
# print("")
# print(req.text)
# print("")
# print(req.headers)

# file = open("youtube.html", "w")
# file.write(req.text)

url = "https://digi24.ro/robots.txt"

req = requests.get(url)

# print(req.text)

sitemap = "https://digi24.ro/sitemaps/sitemap-index.xml"
req = requests.get(sitemap)

soup = BeautifulSoup(req.text, 'xml')
# print(soup.prettify())

locs = soup.find_all("loc")

for loc in locs:
    loc = loc.text
    articles = requests.get(loc)
    articles_soup = BeautifulSoup(articles.text, 'xml')

    articles_urls = articles_soup.find_all("loc")
    for article_url in articles_urls:
        article = requests.get(article_url.text)
        article_soup = BeautifulSoup(article.text, "html.parser")
        title = article_soup.find("h1").text

        print(title)

