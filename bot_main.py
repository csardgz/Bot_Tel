import telebot
from ws_dt_img import capture
from dolartoday_price import precio_today
from bcv_price import precio_bcv
from thread_dt import cap_thread

#tomamos cada hora la captura el precio del $ en dolartoday
tasa_today = cap_thread(capture, precio_today)

# Creamos el bot
print("bot funcionando")
BOT_TOKEN = "bot token"
bot = telebot.TeleBot(BOT_TOKEN)

# Definimos un comando para saludar
@bot.message_handler(commands=["start"])
def saludar(message):
    bot.send_message(message.chat.id, "Bienvenido")

@bot.message_handler(func=lambda message:True)
def mensaje(message):

    
    message_low = message.text.replace("," , ".")
    message_low = message_low.lower()
    if message_low.endswith("$"):
        monto = message_low[0:-1]

        try:
            monto = float(monto)
            bcv = monto*precio_bcv()
            bcv = round(bcv,2)
            bcv = str(bcv)
            DT = monto*tasa_today
            DT = round(DT,2)
            DT = str(DT)
            bot.send_message(message.chat.id, "BCV: " + bcv + "bs")
            bot.send_message(message.chat.id, "DolarToday: " + DT + "bs")
                        
        except ValueError:
            bot.send_message(message.chat.id, "Por favor inserte un monto")


    elif message_low.endswith("bs"):
        monto = message_low[0:-2]
        try:
            monto = float(monto)
            bcv = monto/precio_bcv()
            bcv = round(bcv,2)
            bcv = str(bcv)
            DT = monto/tasa_today
            DT = round(DT,2)
            DT = str(DT)
            bot.send_message(message.chat.id, "BCV: " + bcv + "$")
            bot.send_message(message.chat.id, "DolarToday: " + DT + "$")
                        
        except ValueError:
            bot.send_message(message.chat.id, "Por favor inserte un monto")

    else:
        bot.send_message(message.chat.id, "Por favor escriba segun el formato y use punto decimal. ejemplo: 1.01$ o 1.01bs")





# Iniciamos el bot
if __name__ == "__main__":
    bot.polling(non_stop=True)