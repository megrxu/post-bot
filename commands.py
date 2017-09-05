import telegram, requests, json, utils
from ids import *

# Firse command
def hello(bot, update):
    chat_id = update.message.chat_id
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

# Get random jokes
def laugh(bot, update):
    chat_id = update.message.chat_id
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    headers = {'Accept': 'text/plain'}
    joke = requests.get('https://icanhazdadjoke.com/',headers=headers)
    update.message.reply_text(joke.text)

# Get news from sources
def news(bot, update):
    chat_id = update.message.chat_id
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)

    url_source = 'https://newsapi.org/v1/sources?language=en'
    source_json = requests.get(url_source)
    source_object = json.loads(source_json.text)

    source_list = []
    for item in source_object['sources']:
      source_list.append(telegram.InlineKeyboardButton(item['name'], callback_data=item['id']))

    reply_markup = telegram.InlineKeyboardMarkup(utils.build_menu(source_list, n_cols=2))
    bot.send_message(chat_id=chat_id, text="Please choose a news source", reply_markup=reply_markup).message_id