import requests
from bs4 import BeautifulSoup
import selenium
import flask

# robots = requests.get("https://www.digi24.ro/robots.txt")

# print(robots.text)

# digi_sitemap_index = requests.get("https://www.digi24.ro/sitemaps/sitemap-index.xml")

# print("\n-------------------------------------------------------\n")
# print(digi_sitemap_index.text)

# sitemap_articles_2024_10 = requests.get("https://www.digi24.ro/sitemaps/sitemap-articles-2024-10.xml")

# print("\n-------------------------------------------------------\n")
# print(sitemap_articles_2024_10.text)

# article = requests.get("https://www.digi24.ro/stiri/externe/washington-post-israelul-a-informat-sua-ca-planuieste-o-invazie-terestra-in-liban-2949519")

# print("\n-------------------------------------------------------\n")
# print(article.text)

# file = open("article.html", "w")
# file.write(article.text)


# for i in range(1, 11):
#     page = requests.get(f"https://www.storia.ro/ro/rezultate/vanzare/apartament/bucuresti?page={i}")

#     print(f"Status pagina {i}: {page.status_code}")


# page = requests.get("https://www.storia.ro/ro/rezultate/vanzare/apartament/bucuresti?page=1")
# print(page.text)


digi_sitemap_index = requests.get("https://www.digi24.ro/sitemaps/sitemap-index.xml")

# print("\n-------------------------------------------------------\n")
# print(digi_sitemap_index.text)

soup = BeautifulSoup(digi_sitemap_index.text, "lxml")

print(soup.find_all("loc"))
print(len(soup.find_all("loc")))

for loc in soup.find_all("loc"):
    loc_soup = BeautifulSoup(requests.get(loc.text).text, "lxml")
    print(loc_soup.prettify())

    # print(loc_soup.find_all("loc"))
    # print(len(loc_soup.find_all("loc")))