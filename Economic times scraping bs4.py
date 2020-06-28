import bs4
import requests
import lxml
from bs4 import BeautifulSoup

res = requests.get('https://economictimes.indiatimes.com/archive/year-2002.cms')
soup = BeautifulSoup(res.text,'lxml')

news_box = soup.find('table')
news_box
all_news = news_box.find_all('a')

x = 'https://economictimes.indiatimes.com'+all_news[0].attrs['href']
x

res2 = requests.get(x)
soup = BeautifulSoup(res2.text,'lxml')
print(soup)
in_month = soup.find("table")
#dates = in_month.find_all('a')
#dates