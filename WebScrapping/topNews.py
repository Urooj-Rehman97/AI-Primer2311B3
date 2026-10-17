import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")

news = soup.find_all("h2")

print("Latest News Headlines: \n")

for h in news[:5]:
    print("-", h.text.strip())
# print(news)