import telebot
import dbworker
from telebot import types
import config
import urllib.request
from functions import check_time
from datetime import datetime, time
import logger

bot = telebot.TeleBot(config.TOKEN)


# REPAIR BOT
# @bot.message_handler(func=lambda message: message)
# def send(message):
# 	bot.send_message(message.chat.id, "!")

@bot.message_handler(commands=["start"])
def panel(message):
	keyboard = types.InlineKeyboardMarkup()
	button_add = types.InlineKeyboardButton(text="add", callback_data="add")
	button_get = types.InlineKeyboardButton(text="get", callback_data="get")
	keyboard.add(button_add, button_get)
	bot.send_message(message.chat.id, "Select action", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data=='add')
def entering_login(call):
	bot.send_message(call.from_user.id, "Enter your github login")
	dbworker.set_state(call.from_user.id, config.States.S_LOGIN.value)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id)[0] == config.States.S_LOGIN.value)
def entering_project_name(message):
	dbworker.intering_in_db(message.chat.id, "login", message.text)
	bot.send_message(message.chat.id, "Enter name of repository")
	dbworker.set_state(message.chat.id, config.States.S_PROJECT_NAME.value)


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id)[0] == config.States.S_PROJECT_NAME.value)
def send_file(message):
	dbworker.intering_in_db(message.chat.id, "repository", message.text)

	login = dbworker.get_field(message.chat.id, 'login')[0]
	repository = dbworker.get_field(message.chat.id, 'repository')[0]

	url = f'https://github.com/{login}/{repository}/archive/master.zip'
	print(url)

	dbworker.intering_in_db(message.chat.id, 'url', url)

	urllib.request.urlretrieve(url, f'./downloads/{message.chat.id}.zip')

	with open(f'./downloads/{message.chat.id}.zip',"rb") as f:
		bot.send_document(message.chat.id, f)

	dbworker.intering_in_db(message.chat.id, 'date', str(datetime.now()))

	dbworker.set_state(message.chat.id, config.States.S_SEND_ZIP.value)

@bot.callback_query_handler(func=lambda call: call.data=='get')
def get_file(call):
	if check_time(call.from_user.id):
		with open(f'./downloads/{call.from_user.id}.zip',"rb") as f:
			bot.send_document(call.from_user.id, f)
		bot.send_message(call.from_user.id, dbworker.get_field(call.from_user.id, 'date')[0])

	else:
		urllib.request.urlretrieve(url, f'./downloads/{call.from_user.id}.zip')

		with open(f'./downloads/{call.from_user.id}.zip',"rb") as f:
			bot.send_document(call.from_user.id, f)

		dbworker.intering_in_db(message.chat.id, 'date', str(datetime.now()))

	dbworker.set_state(call.from_user.id, config.States.S_SEND_ZIP.value)


bot.remove_webhook()
bot.polling(none_stop=True)
