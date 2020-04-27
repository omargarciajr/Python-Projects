import bs4
import sys
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

news_url = "https://news.google.com/news/rss"
Client = urlopen(news_url)
xml_page = Client.read()
Client.close()

soup_page = soup(xml_page, "xml")
news_list = soup_page.findAll("item")

sys.stdout = open("Articles.txt", "w")

#print news title, url and publication date

for id, news in enumerate(news_list, 1):
    print("\n")
    print(id, " ", news.title.text)
    print(news.link.text)
    print(news.pubDate.text)
    print("-"*60)

sys.stdout.close()