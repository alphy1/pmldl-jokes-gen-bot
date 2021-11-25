import requests as rq
from datetime import timedelta, datetime
from bs4 import BeautifulSoup as bs
import pandas as pd

# URL = "https://www.anekdot.ru/release/story/year/{year}/{page}"
URL = "https://www.anekdot.ru/release/anekdot/day/{date}/"  # in format 1996-12-30
HEADERS = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
}

def get_anekdots(url):
    res = rq.get(url, headers=HEADERS)
    if res.status_code != 200:
        print(res.text)
        return []

    parser = bs(res.text, "html.parser")
    texts = parser.select(".topicbox > div.text")
    texts = [text.text for text in texts]
    votes = parser.select(".topicbox > div.votingbox > .rates")
    votes = [int(vote.get("data-r", "0").split(";")[0]) for vote in votes]

    return list(zip(texts, votes))


start = datetime(year=1995, month=1, day=1)
# start = datetime(year=2021, month=9, day=30)
end = datetime.now()
d = timedelta(days=1, )

anekdots = []

while start <= end:
    date = start.strftime("%Y-%m-%d")

    anekdots.extend(get_anekdots(URL.format(date=date)))

    start += d

anekdots = pd.DataFrame(anekdots, columns=["text", "rate"])
anekdots.to_csv("anekdotyru.csv")