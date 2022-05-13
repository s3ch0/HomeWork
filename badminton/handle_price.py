import requests
from __const import *
from luck.embellish import printf
from rich.progress import track
from bs4 import BeautifulSoup

price_list = []

cells_list = load_pkl('cells.pkl')

if __name__ == '__main__':
    for i in track(range(len(cells_list)), description="Processing..."):
        index = cells_list[i].link.split('/')[-1].split('.')[0].split('_')[-1]
        url = THE_PRICE_URL_TEMPLATE.format(index)
        resp = requests.get(url, timeout=30)
        soup = BeautifulSoup(resp.text, 'lxml')
        price = soup.find_all('strong', class_='bluetext2')
        price_list.append(
            Price(price[0].text.strip(), price[1].text.strip(),
                  price[2].text.strip()))
        printf(price_list[i])

# save the price_list
    price_data = open('price.pkl', 'wb')
    pickle.dump(price_list, price_data)
    price_data.close()
    printf("Complete!")

    print(len(price_list))
