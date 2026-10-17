import requests

url = "https://www.python.org/"

response = requests.get(url)

# print(response.text)

from bs4 import BeautifulSoup

html = response.text
soup = BeautifulSoup(html, "html.parser")

print(soup.title.text)