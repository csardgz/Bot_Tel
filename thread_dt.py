import threading
import time


def cap_thread(capture, precio_today):

    tasa_dt = precio_today()

    def f_int():
        
        while True:
            global tasa_dt
            print("buscando imagen en DolarToday cada 50s")
            capture()
            tasa_dt = precio_today()
            print(f"tasa_dt es = {tasa_dt}")
            #Tiempo de esperar para recargar informacion de dolartoday
            time.sleep(3600)

    t = threading.Thread(target = f_int)
    t.start()
    return tasa_dt
