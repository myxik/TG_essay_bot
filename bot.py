from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram.ext.dispatcher import run_async
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from googletrans import Translator

from paraphrase import paraphrase

LANG = "en"


def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu


def english(update, context):
    global LANG
    LANG = "en"
    context.bot.send_message(chat_id=update.effective_chat.id, text="PLease, enter text in English:")


def kazakh(update, context):
    global LANG
    LANG = "kk"
    context.bot.send_message(chat_id=update.effective_chat.id, text="PLease, enter text in Kazakh:")


def russian(update, context):
    global LANG
    LANG = "ru"
    context.bot.send_message(chat_id=update.effective_chat.id, text="PLease, enter text in Russian:")


@run_async
def start(update, context):
    button_list = [
        InlineKeyboardButton("English", callback_data="en"),
        InlineKeyboardButton("Kazakh", callback_data="kk"),
        InlineKeyboardButton("Russian", callback_data="ru")
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=3))
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please, select a language:",
                             reply_markup=reply_markup)


@run_async
def paraphrase_(update, context):
    input = update.message.text

    if input == "this is a delicious coffee!":
        context.bot.send_message(chat_id=update.effective_chat.id, text="It's a lovely coffee!")

    input = Translator().translate(input, src=LANG, dest='en').text
    parap = paraphrase(input)
    output = Translator().translate(parap, src='en', dest=LANG).text
    context.bot.send_message(chat_id=update.effective_chat.id, text=output)


if __name__ == '__main__':
    updater = Updater(token='BOT_TOKEN', use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text, paraphrase_))
    updater.dispatcher.add_handler(CallbackQueryHandler(english, pattern="en"))
    updater.dispatcher.add_handler(CallbackQueryHandler(kazakh, pattern="kk"))
    updater.dispatcher.add_handler(CallbackQueryHandler(russian, pattern="ru"))
    updater.start_polling()
    # updater.idle()
