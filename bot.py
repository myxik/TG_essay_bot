from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters
from telegram.ext.dispatcher import run_async

@run_async
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

@run_async
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


if __name__ == '__main__':
    updater = Updater(token='915083921:AAGaVlWApWVybAD-7WJoatVUoL4vhT_cYFA', use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(Filters.text, echo)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()
    # updater.idle()
