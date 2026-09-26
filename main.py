import requests
from bs4 import BeautifulSoup
import time

all_quotes = []

for page_num in range(1, 11):
    url = f"http://quotes.toscrape.com/page/{page_num}/"
    print(f"Парсим страницу {page_num}: {url}")

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes_divs = soup.find_all("div", class_="quote")

    for div in quotes_divs:
        text = div.find("span", class_="text").text
        author = div.find("small", class_="author").text
        tags = div.find_all("a", class_="tag")
        tag_list = [tag.text for tag in tags]
        line = f"{author}: {text} | Теги: {', '.join(tag_list)}"
        all_quotes.append(line)

    print(f"Найдено цитат на странице: {len(quotes_divs)}")
    time.sleep(1)

with open("quotes.txt", "w", encoding="utf-8") as file:
    for line in all_quotes:
        file.write(line + "\n")

print(f"Готово! Собрано цитат: {len(all_quotes)}")
