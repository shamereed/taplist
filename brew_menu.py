import urllib.request
import argparse
from bs4 import BeautifulSoup

bar_list = {
    'foundry': 'http://cs-tf.com/beer-selection/',
    'ten bells': 'a',
    'enos': 'b',
    'libertine': 'c',
    'wild detectives': 'd'
}

def get_brews(bar):
    req = urllib.request.Request(bar)
    page = urllib.request.urlopen(req)
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find('table', {'class': 'wikitable sortable'})
    beers = []
    for row in table.findAll('tr'):
        col = row.findAll('td')
        if len(col) > 0:
            beers.append(str(col[0].string.strip()))
    beers.sort()
    return beers


def get_stock_prices(beers_list):
    for beer in beers_list:
        htmlfile = urllib.request.urlopen(
            "http://finance.yahoo.com/q?s={0}".format(beer)
        )
        htmltext = htmlfile.read()
        soup = BeautifulSoup(htmltext, 'html.parser')
        htmlSelector = 'yfs_l84_{0}'.format(beer.lower())
        for price in soup.find_all(id=htmlSelector):
            print('{0} is {1}'.format(beer, price.text))


def main():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    
    get_brews(bar_list)

if __name__ == '__main__':
    main()
