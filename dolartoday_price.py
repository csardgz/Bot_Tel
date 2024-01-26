import easyocr

#Busca el precio de la tasa bs/$ de la imagen que publica la pagina de dolartoday

def precio_today():

    reader = easyocr.Reader(['en'])
    result = reader.readtext("precio_today.jpg",detail=0)
    usdbs = result[6][-5:].replace(",", ".")
    usdbs = float(usdbs)

#retorna un float con el valor de la tasa bs/$ de dolar today
    return usdbs