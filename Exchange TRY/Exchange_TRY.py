import requests
from bs4 import BeautifulSoup
import sys

url = "https://www.doviz.com/"

page = requests.get(url).content

soup = BeautifulSoup(page, "html.parser")


def exchange_currency(currency):
    dollar = soup.find_all("span", {"data-socket-key": currency})
    dollar = dollar[0].text
    print(dollar)


currency = input("What do you want to convert your money from Turkish lira to? ")


try:
    """
    Dollar = "USD"
    Euro = "EUR
    """
    exchange_currency(currency)
except IndexError:
    sys.stderr.write("Wrong string entered!!")
    sys.stderr.flush()
