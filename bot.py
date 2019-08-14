from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext.filters import Filters
from save_numbers import save_numbers, read_numbers

waiting = None

def save_numbers_view(update):
    try:
        num_pip, num_veg = [int(i) for i in update.message["text"].split("\n")]
        res = save_numbers(num_pip, num_veg)
        if res:
            global waiting
            waiting = None
            update.message.reply_text('Ok')
        else:
            update.message.reply_text('введены некорректеые данные, попробуйте еще раз пожалуйста')
    except:
        update.message.reply_text('введены некорректеые данные, попробуйте еще раз пожалуйста')

def hello(bot, update):
    print(bot)
    print(update.message['text'])
    update.message.reply_text('Hello, my friend')

def answerer(bot, update):
    if waiting is None:
        update.message.reply_text('use commands, please!')
    else:
        waiting(update)

def loading_number(bot, update):
    global waiting
    waiting = save_numbers_view
    update.message.reply_text('введи пожалуйста колличество людей и вегатерианцев')


updater = Updater('691587351:AAFPHlZgoGGCIXmOIPS4I1KvfI8iAbBtIts')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('loading_number', loading_number))

updater.dispatcher.add_handler(MessageHandler(Filters.text, answerer))

updater.start_polling()
updater.idle()