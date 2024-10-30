from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import csv
from datetime import datetime


options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get("https://www.emag.ro/")
#<button class="btn btn-primary btn-block js-accept gtm_h76e8zjgoo">Accept toate </button>
time.sleep(2)

accept_cookies = driver.find_element(By.CLASS_NAME, "js-accept")
accept_cookies.click()

time.sleep(1)
# <input type="search" id="searchboxTrigger" name="query" class="searchbox-main gtm_search_bar_click_search_week js-searchbox-input" placeholder="Începe o nouă căutare" autocomplete="off">
search_bar = driver.find_element(By.ID, "searchboxTrigger")
search_bar.send_keys("laptop")
search_bar.send_keys(Keys.ENTER)

time.sleep(1)

data = []

def extract_from_card_grid(drv, index):
    print(f"SCRAPING PAGE {index}")
    if index > 1:
        drv.get(f"https://www.emag.ro/laptopuri/p{index}/c")

    card_grid = drv.find_element(By.ID, "card_grid")
    print(card_grid)

    cards = card_grid.find_elements(By.CLASS_NAME, "card-item")
    print(len(cards))

    for card in cards: 
        info = card.find_element(By.CLASS_NAME, "card-v2-info")
        #card-v2-title
        title = card.find_element(By.CLASS_NAME, "card-v2-title")
        print(title.text)
        price = card.find_element(By.CLASS_NAME, "product-new-price")
        print(price.text)
        obj = {"title": title.text, "price": price.text}
        data.append(obj)

for i in range(1,10):
    extract_from_card_grid(driver, i)

print(data)

with open(f"laptops_{datetime.now()}.csv", "w") as file: 
    writer = csv.DictWriter(file, fieldnames=["title", "price"])
    writer.writeheader()
    for row in data: 
        writer.writerow(row)


time.sleep(100)