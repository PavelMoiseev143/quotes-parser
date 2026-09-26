import requests
from bs4 import BeautifulSoup
import time

all_quotes = []

url = "http://quotes.toscrape.com/page/1/"
page_num = 1

while url:
    print(f"Парсим страницу: {page_num}: {url}")

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

    next_button = soup.find("li", class_="next")
    if next_button:
        next_href = next_button.find("a")["href"]
        url = f"http://quotes.toscrape.com{next_href}"
        page_num += 1
    else:
        url = None

    time.sleep(1)

with open("quotes.txt", "w", encoding="utf-8") as file:
    for line in all_quotes:
        file.write(line + "\n")

print(f"Готово! Собрано цитат: {len(all_quotes)}")

