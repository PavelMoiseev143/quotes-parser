from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
import csv

driver = webdriver.Chrome()
driver.get("http://quotes.toscrape.com/js/")
time.sleep(2)

all_quotes = []

while True:
    quotes_divs = driver.find_elements(By.CLASS_NAME, "quote")
    print(f"Найдено цитат: {len(quotes_divs)}")

    for div in quotes_divs:
        text = div.find_element(By.CLASS_NAME, "text").text
        author = div.find_element(By.CLASS_NAME, "author").text
        tags = div.find_elements(By.CLASS_NAME, "tag")
        tag_list = [tag.text for tag in tags]
        all_quotes.append([author, text, ", ".join(tag_list)])
    try:
        next_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Next")
        next_button.click()
        time.sleep(2)
    except NoSuchElementException:
        print("Это была последняя страница")
        break

with open("quotes_js.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Автор", "Цитата", "Теги"])
    for quote in all_quotes:
        writer.writerow(quote)

print(f"Готово! Собрано цитат: {len(all_quotes)}")

driver.quit()
