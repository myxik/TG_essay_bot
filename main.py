from telegram.ext import Updater
from telegram.ext import CommandHandler


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


if __name__ == '__main__':
    updater = Updater(token='915083921:AAGaVlWApWVybAD-7WJoatVUoL4vhT_cYFA', use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    updater.start_polling()
