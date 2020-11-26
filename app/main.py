from flask import Flask, request, jsonify
from bot import bot
import telebot
import config

app = Flask(__name__)

# bot = telebot.TeleBot(config.TOKEN)

def main():
    bot.polling(none_stop=True)

if __name__ == "__main__":
    main()


"""

WEBHOOK_HOST = '127.0.0.1'
WEBHOOK_PORT = 443
WEBHOOK_LISTEN = '0.0.0.0'
WEBHOOK_URL_BASE = f"https://{WEBHOOK_HOST}:{WEBHOOK_PORT}"
WEBHOOK_URL_PATH = '/bot/'

def main():

    if config.DEBUG==1:

        run_with_ngrok(app)

        @app.route(WEBHOOK_URL_PATH, methods=['POST'])
        def getMessage():
            if request.headers.get('content-type') == 'application/json':
                json_string = request.get_data().decode('utf-8')
                update = telebot.types.Update.de_json(json_string)
                bot.process_new_updates([update])
                return '!', 200

        @app.route("/")
        def webhook():
            bot.remove_webhook()
            bot.set_webhook(url=WEBHOOK_URL_BASE+WEBHOOK_URL_PATH)

        app.run(host=WEBHOOK_LISTEN, port=WEBHOOK_PORT)

    else:
        bot.remove_webhook()
        bot.polling(none_stop=True)


if __name__ == "__main__":
    bot.polling(none_stop=True)
"""

