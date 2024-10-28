from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import csv
from datetime import datetime

options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get("https://www.olx.ro/")

print("Running headless browser")


accept_cookies = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
time.sleep(2)
accept_cookies.click()

time.sleep(1)
search = driver.find_element(By.ID, 'search')
search.send_keys('apartament 2 camere')
search.send_keys(Keys.ENTER)

articles = []

def get_articles():
    # 
    # <div data-testid="listing-grid" class="css-j0t2x2">
    # card articol - css-qfzx1y

    # card title - css-u2ayx9
    time.sleep(2)
    page_source = driver.find_element(By.TAG_NAME, 'html').get_attribute('innerHTML')
    page_soup = BeautifulSoup(page_source, "html.parser")

    # file = open("source.html", "w")
    # file.write(page_soup.prettify())

    cards = page_soup.find_all('div', class_="css-u2ayx9")
    article = {}
    for card in cards: 
        title = card.find('h6').text 
        price = card.find('p').text 
        article = { "title": title, "price": price }
        articles.append(article)

        print(title + ": " + price)

time.sleep(2)
# https://www.olx.ro/oferte/q-apartament-2-camere/?page=2
get_articles()
for i in range(2, 25):
    driver.get(f"https://www.olx.ro/oferte/q-apartament-2-camere/?page={i}")
    print("Scraping page " + str(i))
    get_articles()


driver.quit()
print("Done scraping!")

with open(f"articles_{datetime.now()}.csv", mode="w") as csvfile:
    fieldnames = ["title", "price"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for article in articles:
        writer.writerow(article)