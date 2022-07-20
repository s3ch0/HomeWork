import requests
from __const import *
from rich.progress import track
from luck.__log import Log
from bs4 import BeautifulSoup

price_list = []
CRAWL_PRICE_LOG = Log()
cells_list = load_pkl('./Data/cells.pkl')

if __name__ == '__main__':

    index_list = [
        cell.link.split('/')[-1].split('.')[0].split('_')[-1]
        for cell in cells_list
    ]
    CRAWL_PRICE_LOG.info("Will crawl price for {} cells".format(
        len(cells_list)))
    for i in track(range(len(cells_list)), description="Processing..."):
        index = cells_list[i].link.split('/')[-1].split('.')[0].split('_')[-1]
        url = THE_PRICE_URL_TEMPLATE.format(index)
        resp = requests.get(url, timeout=30)
        soup = BeautifulSoup(resp.text, 'lxml')
        price = soup.find_all('strong', class_='bluetext2')
        price_list.append(
            Price(price[0].text.strip(), price[1].text.strip(),
                  price[2].text.strip()))
        #  CRAWL_PRICE_LOG.process("Crawled price for {}".format(i))

    # save the price_list
    price_data = open('price.pkl', 'wb')
    pickle.dump(price_list, price_data)
    price_data.close()
    CRAWL_PRICE_LOG.complete("Crawl price complete!")

    print(len(price_list))
