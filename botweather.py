import pyowm 
import telebot

owm = pyowm.OWM('027d75f49b5de85a66211f3b26f69d82', language = "ru")
bot = telebot.TeleBot("723955745:AAHtAdrt3mTu11aVBzAldOOvQKPyzXOjdDk")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place(message.text)
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]

	answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
	answer += "Температура : " + str(temp) + "\n\n"

	if temp  < 10:
		answer += "Одень куртку, холодно" 
	elif temp < 20:
		answer += "Натяни толстовку" 
	else: 
		answer += "Жарковато" 

	bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )