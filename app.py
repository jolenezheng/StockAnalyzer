import requests
from bs4 import BeautifulSoup 

BASE_URL = "https://ca.finance.yahoo.com/quote/"

my_tickers = ['QUIS.V', 'TD.TO', 'AAPL', 'XOM', 'WFC', 'GOOG']

for ticker in my_tickers:
  URL = BASE_URL + ticker
  r = requests.get(URL) 

  soup = BeautifulSoup(r.content, 'html5lib') 

  price_header = soup.find('div', attrs = {'id':'quote-header-info'})
  price = price_header.find_all('span')[1].text
  print(ticker + "'s current price: " + price)
