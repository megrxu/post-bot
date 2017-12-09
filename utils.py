import commands, subprocess
from ids import *
import random
from data import Hans 


def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [[buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu[0]


def get_post(bot, update):
    msg = update.message
    if (msg['photo']):
        file = bot.getFile(msg['photo'][-1]['file_id'])
        path = file['file_path']
        subprocess.call(['mkdir', 'message_files/pics'])
        subprocess.call(['wget', path, '-P', 'message_files/pics/'])

def chat_dispatcher(bot, update):
    #If it is authorized user
    authorized_ids = [TyteKa]
    if update.message.chat_id in authorized_ids:
        get_post(bot, update)
        commands.post(bot, update)
    else:
        commands.echo(bot, update)
        
def callback_dispatcher(bot, update):
    call_str = update.callback_query['data'].split('/')
    chat_id = update.callback_query['message']['chat']['id']
    message_id = update.callback_query['message']['message_id']
    if call_str[0] == 'post':
        if (int(call_str[1])):
            commands.dopost(bot, update)
            bot.answer_callback_query(callback_query_id=update.callback_query.id, text='Posted.')
            bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Posted.')
        else:
            bot.answer_callback_query(callback_query_id=update.callback_query.id, text='Canceled.')
            bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Canceled.')
    elif call_str[0] == 'news':
        bot.answer_callback_query(callback_query_id=update.callback_query.id, text='Here you go.')        
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Here\'s the news.')
        commands.send_news(bot, update, call_str[1])
        
def randomCN():
    num = random.sample(list(range(5, 20)), 1)
    return "".join(random.sample(Hans, num[0]))