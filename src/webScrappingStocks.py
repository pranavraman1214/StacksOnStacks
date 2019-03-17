from bs4 import BeautifulSoup
import requests
from selenium import webdriver

key_stats_on_main =['Market Cap', 'PE Ratio (TTM)', 'EPS (TTM)']
key_stats_on_stat =['Enterprise Value', 'Trailing P/E', 'Forward P/E',
                     'PEG Ratio (5 yr expected)', 'Return on Assets', 'Quarterly Revenue Growth',
                     'EBITDA', 'Diluted EPS', 'Total Debt/Equity', 'Current Ratio']

page_link = "https://finance.yahoo.com/quote/SIRI/key-statistics?p=SIRI"
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")
textContent = []
data = []
searchString = "tr"
for i in range(len(page_content.find_all(searchString))):
    paragraphs = page_content.find_all(searchString)[i].text
    textContent.append(paragraphs)
for name in textContent:
    print (name)





