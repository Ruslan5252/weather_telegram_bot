import pyowm
from pyowm import OWM
from pyowm.utils.config import get_default_config
import telebot

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('bc3e62293cb831488ebd6acffa6ccddb')
bot = telebot.TeleBot("1694221610:AAH85FF52hik-AbzHkGU-cF4PZcYEriG5qs")


@bot.message_handler(content_types=['text'])
def send_echo(message):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]
    wind = w.wind()
    humidity = w.humidity
    answer = "В городе " + message.text + " Сейчас " + str(w.detailed_status) + '\n\n'
    answer += "Температура: " + str(temp) + '\n'
    answer += "Скорость ветра " + str(wind['speed']) + '\n'
    answer += "Влажность воздуха " + str(humidity) + '%' + '\n'
    if temp < 10:
        answer += "Очень холодно, оденься нормально"
    elif temp < 20:
        answer += "На улице  прохладно"
    else:
        answer += "На улице очень тепло "

    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)
