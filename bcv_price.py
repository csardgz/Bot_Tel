from bs4 import BeautifulSoup
import requests


def precio_bcv():
    url = 'https://www.bcv.org.ve/'

    response = requests.get(url, verify=False)
    text = response.text

    soup = BeautifulSoup(text, "lxml")
    divs = soup.find("div", {"id": "dolar"})
    usd = divs.get_text()
    usd_list = usd.split()
    usd_precio = usd_list[1].replace(",", ".")
    tasa_bcv = float(usd_precio)

    return tasa_bcv