import requests
from bs4 import BeautifulSoup

#captura la imagen de dolartoday donde publican los precios de las tasas de cambio
def capture():
    url2 = 'https://dolartoday.com/'

    response2 = requests.get(url2, verify=False)
    text2 = response2.content

    soup2 = BeautifulSoup(text2, "lxml")
    divs2 = soup2.find("img", class_ = "wp-image-486948")

    res_img = requests.get(divs2.get("src"))
    img_data = res_img.content


    with open("precio_today.jpg", "wb") as f:
        f.write(img_data)
    
    return