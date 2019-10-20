# coding: utf8
import telebot
import constants as cons
import newmath as math
from datetime import datetime
from flask import Flask, request

bot = telebot.TeleBot(cons.mytoken)
bot.remove_webhook()
bot.set_webhook(url = 'https://{}'.format(cons.sevurl))
app = Flask(__Name__)
#bot.send_message(cons.myid, 'Welcome Master!')

def log(message, final_answer):
	print(datetime.now())
	#print('Message from {0} {1} (id = {2})'.format(message.from_user.first_name, 
																#message.from_user.last_name, 
																#str(message.from_user.id)))
	try:
		print(message.from_user.first_name,' ',message.from_user.last_name,' ',message.from_user.id)
		print('Text: ' + message.text)
		print('Answer: ', final_answer)
	except:
		print('Answer: ', final_answer)
@app.route('/{}'.format(cons.sevurl), methods = ["Post"])
@bot.message_handler(content_types=['text'])
def handle_text(message):
	'''if message.text.encode('utf8') == "id":
		bot.send_message(message.chat.id, message.chat.id)'''
	input_answer = 'None'
	try:
		all_answer = math.Request(message.text)
		all_answer = math.Split_String(all_answer)
		input_answer = math.Find_Input(all_answer).replace('&apos;', '\'')
		limit_answer = math.Find_Limit(all_answer)
		sum_answer = math.Find_Sum(all_answer)
		roots_answer = math.Find_Roots(all_answer)
		decimal_answer = math.Find_Decimal(all_answer)
		result_answer = math.Find_Result(all_answer)
		integ_answer = math.Find_Integ(all_answer)
		'''if input_answer == 'None':
			input_answer = message.text'''
		if limit_answer != 'None' and roots_answer == 'None':
			final_answer = 'Your Input: ' + message.text + '\n' + 'Goes to: ' + limit_answer + '\n'
		elif sum_answer != 'None' and decimal_answer == 'None':
				final_answer = 'Your Input: ' + message.text + '\n' + 'Equals: ' + sum_answer + '\n'
		elif '\'' in input_answer:
			final_answer = 'For derivative don\'t use {\'} in your Request'
		elif integ_answer != 'None':
			final_answer = 'Your Input: ' + message.text + '\n' + 'Integral: ' + integ_answer + '\n'
		elif input_answer == 'None' and limit_answer == 'None' and sum_answer == 'None' and result_answer == 'None' and integ_answer == 'None':
			final_answer = 'шо?'

		else:
			input_answer = message.text
			final_answer = 'Your Input: ' + input_answer + '\n'
			#roots_answer = math.Find_Roots(all_answer)
			if roots_answer != 'None':
				final_answer = final_answer + 'Roots: ' + roots_answer + '\n'
			if result_answer != 'None':
				final_answer = final_answer + 'Equals: ' + result_answer + '\n'
			solution_answer = math.Find_Solution(all_answer)
			if solution_answer != 'None':
				final_answer = final_answer + 'Roots: ' + solution_answer + '\n'
			if limit_answer != 'None':
				final_answer = final_answer + 'Goes to: ' + limit_answer + '\n'
			if sum_answer != 'None':
				final_answer = final_answer + 'Equals: ' + sum_answer + '\n'
			if decimal_answer != 'None':
				final_answer = final_answer + 'Decimal: ' + decimal_answer + '\n'
			deriva_answer = math.Find_Deriva(all_answer)
			if deriva_answer != 'None':
				final_answer = final_answer + '1.Derivative: y\'=' + deriva_answer + '\n'
				try:
					new_answer = math.Request('y=' + deriva_answer)
					new_answer = math.Split_String(new_answer)
					deriva2_answer = math.Find_Deriva(new_answer)
					if deriva2_answer != 'None':
						final_answer = final_answer + '2.Derivative: y\"=' + deriva2_answer + '\n'
				except:
					final_answer = final_answer
			lmax_answer = math.Find_Lmax(all_answer)
			if lmax_answer != 'None':
				final_answer = final_answer + 'Local max: y ' + lmax_answer + '\n'
			gmax_answer = math.Find_Gmax(all_answer)
			if gmax_answer != 'None':
				final_answer = final_answer + 'Global max: y ' + gmax_answer + '\n'
			lmin_answer = math.Find_Lmin(all_answer)
			if lmin_answer != 'None':
				final_answer = final_answer + 'Local min: y ' + lmin_answer + '\n'
			gmin_answer = math.Find_Gmin(all_answer)
			if gmin_answer != 'None':
				final_answer = final_answer + 'Global min: y ' + gmin_answer + '\n'

	except:
		final_answer = 'Ne shary na russkom'

	if message.text == '/start':
		final_answer = 'Here we go!'
	bot.send_message(message.chat.id, final_answer)
	try:
		log(message, final_answer)
		#print(message.text)
	except:
		print('_Foreign_')

bot.polling(none_stop = True, interval = 0)