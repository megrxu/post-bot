import telegram, requests, json, utils, subprocess, facebook
from ids import *

# First command
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

    name_list = ['BBC News', 'Buzzfeed', 'CNN', 'Engadget', 'Google News', 'Hacker News', 'National Geographic', 'The Economist', 'The Telegraph', 'The Verge', 'The Washington Post', 'Time', 'USA Today']
    source_list = []
    for item in source_object['sources']:
        if(item['name'] in name_list):
            source_list.append(telegram.InlineKeyboardButton(item['name'], callback_data='news/' + item['id']))

    reply_markup = telegram.InlineKeyboardMarkup(utils.build_menu(source_list, n_cols=2))
    bot.send_message(chat_id=chat_id, text="Please choose a news source", reply_markup=reply_markup).message_id

def send_news(bot, update, name):
    chat_id = update.callback_query.from_user.id
    bot.answer_callback_query(callback_query_id=update.callback_query.id, text='Here you go!')
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    source = name
    url = 'https://newsapi.org/v1/articles?source={source}&apiKey={apiKey}'.format(source=source, apiKey=news_api)
    news_json = requests.get(url)
    news_object = json.loads(news_json.text)
    for item in news_object['articles']:
        text = ('*{title}*\n[Link]({link})'.format(title=item['title'], link=item['url']))
        bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.MARKDOWN, disable_web_page_preview=False)

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def post(bot, update):
    chat_id = update.message.chat_id
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    source_list = [
        telegram.InlineKeyboardButton('Yes!', callback_data='post/1'),
        telegram.InlineKeyboardButton('No', callback_data='post/0')
    ]

    reply_markup = telegram.InlineKeyboardMarkup(utils.build_menu(source_list, n_cols=2))
    bot.send_message(chat_id=chat_id, text="Would you like to post it?", reply_markup=reply_markup, reply_to_message_id=update.message.message_id)

    file_object = open('message_meta.py', 'w')
    try:
        file_object.write(str(update.message))
    finally:
        file_object.close()

def dopost(bot, update):
    # Post
    # Channel
    chat_id = update.callback_query['message']['chat']['id']
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    graph = facebook.GraphAPI(access_token=facebook_auth_token, version="2.1")
    chat_id = TyteKaChannel

    file_object = open('message_meta.py', 'r')
    try:
        msg_str = file_object.read()
    finally:
          file_object.close()
    msg = eval(msg_str)

    if (not msg['photo']):
        # On channel
        bot.send_message(chat_id=chat_id, text=msg['text'])
        # On facebook
        graph.put_object(
            parent_object="me",
            connection_name="feed",
            message=msg['text'])
    else:
        file = bot.getFile(msg['photo'][-1]['file_id'])
        path = file['file_path']
        bot.send_photo(chat_id=chat_id, photo=msg['photo'][-1]['file_id'], caption=msg['caption'] if 'caption' in msg.keys() else None)
        # print('message_files/pics/' + path.split('/')[-1])
        graph.put_photo(image=open('message_files/pics/' + path.split('/')[-1], 'rb'), message=msg['caption'] if 'caption' in msg.keys() else 'No caption.')

    subprocess.call(['rm', 'message_files', '-rf'])
    subprocess.call(['mkdir', 'message_files'])
