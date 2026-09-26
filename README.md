# Quotes Parser

Парсер цитат с сайта [quotes.toscrape.com](http://quotes.toscrape.com/).
Собирает цитаты, авторов и теги со всех 10 страниц и сохраняет в файл `quotes.txt`.

## Установка

```bash
pip install requests beautifulsoup4
```

## Запуск

```bash
python parser.py
```

## Результат

Все цитаты сохраняются в файл `quotes.txt` в формате:

```
Автор: Текст цитаты | Теги: tag1, tag2, tag3
```

## Технологии

- Python 3
- requests — HTTP-запросы
- BeautifulSoup4 — парсинг HTML
