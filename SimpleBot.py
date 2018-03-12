# coding: utf8
'''Obviously extremely simple bot'''
import telebot

bot = telebot.TeleBot(mytoken) #instead {mytoken} insert token given u by BotFather during the registration
@bot.message_handler(content_types=['text'])
	def handle_text(message):
		if message.text.encode('utf8') == 'some language except english':
			final_answer = 'respectively an answer'
		 elif message.text == 'some english stuff':
			final_answer = 'and some other answer'

	bot.send_message(message.from_user.id, final_answer)
bot.polling(none_stop = True, interval = 0)