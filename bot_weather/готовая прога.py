import pyowm
import telebot

owm = pyowm.OWM('bc3e62293cb831488ebd6acffa6ccddb')
bot = telebot.TeleBot("1694221610:AAH85FF52hik-AbzHkGU-cF4PZcYEriG5qs")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation=owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature("celsius")["temp"]
    wind = w.wind()
    answer= "В городе " + message.text + "Сейчас" + w.get_detailed_status()
    answer+= "Температура сейчас в районе " + str(temp)+"\n\n"
    answer+="Скорость ветра " +str(wind)

    if temp<10:
        answer+="Очень холодно , одевайся ппц как тепло ! "
    elif temp<20:
        answer+="На улице прохладно , оденься потеплее"
    else:
        answer+="Сейчас очень тепло, одевай что угодно "
    bot.send_message(message.chat.id,answer)
bot.polling(none_stop= True)
