from datetime import datetime
import requests
from bs4 import BeautifulSoup


def parse(url="https://ufa.flamp.ru/firm/vkusno_i_tochka-2393065583018885"):

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "lxml")

    articles = soup.find_all("article")

    json_data = {}

    for article in articles:
        id = article.get("data-entity-id")
        author = article.find("cat-brand-name").get("name")
        date = datetime.strptime(article.find("cat-brand-ugc-date").get("date"), '%Y-%m-%dT%H:%M:%S%z').strftime('%Y-%m-%d %H:%M:%S')
        rate = article.find("li", class_="review-estimation__item list__item t-text t-text--micro t-text--bold review-estimation__item--checked").text.strip()
        text = article.find("p", class_="t-rich-text__p").text.strip()

        json_data[id] = {"author": author, "date": date, "rate": rate, "text": text}

    return json_data
