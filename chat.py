import telegram, utils
from ids import *
import subprocess

# If others, echo
def check(bot, update):
    chat_id = update.message.chat_id
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)    
    if (chat_id != TyteKa):
        echo(bot, update, chat_id)
    else:
        post(bot, update, chat_id)

def echo(bot, update, chat_id):
    bot.send_message(chat_id=chat_id, text=update.message.text)

# If it is me, post something
def post(bot, update, chat_id):
    source_list = [
        telegram.InlineKeyboardButton('Yes!', callback_data='y'),
        telegram.InlineKeyboardButton('No', callback_data='n')
    ]

    reply_markup = telegram.InlineKeyboardMarkup(utils.build_menu(source_list, n_cols=2))
    bot.send_message(chat_id=chat_id, text="Would you like to post it?", reply_markup=reply_markup, reply_to_message_id=update.message.message_id)

    subprocess.call(['rm', 'message_files', '-rf'])
    subprocess.call(['mkdir', 'message_files'])

    file_object = open('message_meta.py', 'w')
    try:
        file_object.write(str(update.message))
    finally:
        file_object.close()
