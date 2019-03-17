from bs4 import BeautifulSoup
import requests
from selenium import webdriver
ema50 = ""
ema200 = ""
page_link = "https://finance.yahoo.com/quote/SIRI/key-statistics?p=SIRI"
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")
textContent = []
data = []
searchString = "td"
for i in range(len(page_content.find_all(searchString))):
    paragraphs = page_content.find_all(searchString)[i].text
    textContent.append(paragraphs)

for i in range(len(textContent)):
    if i % 2 != 0:
        data.append(textContent[i])

for i in range(len(data)):
    print (data[i])





