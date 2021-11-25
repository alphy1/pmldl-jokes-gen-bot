import requests as rq
from datetime import timedelta, datetime
from bs4 import BeautifulSoup as bs
import pandas as pd

URL = "https://nekdo.ru/date/{date}/"  # in format ddmmyy

def get_anekdots(url):
    res = rq.get(url)
    if res.status_code != 200:
        print(res.text)
        return []

    parser = bs(res.text, "html.parser")
    texts = parser.select("div.text")
    texts = [text.text for text in texts]
    votes = parser.select("span.like")
    votes = [vote.text for vote in votes]
    return list(zip(texts, votes))


start = datetime(year=2017, month=3, day=26)
end = datetime.now()
d = timedelta(days=1, )

anekdots = []

while start <= end:
    date = start.strftime('%d%m%y')
    anekdots.extend(get_anekdots(URL.format(date=date)))
    start += d
anekdots = pd.DataFrame(anekdots, columns=["text", "rate"])
anekdots.to_csv("nekdoru.csv")