import telegram, requests, json, utils, subprocess, facebook
from ids import *
import tweepy

# First command
def hello(bot, update):
    chat_id = update.message.chat_id
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

# Get random hans
def hans(bot, update):
    chat_id = update.message.chat_id
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    text = utils.randomCN()
    update.message.reply_text(text)

# Get random zen
def zen(bot, update):
    chat_id = update.message.chat_id
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    zen = requests.get('https://api.github.com/zen')
    update.message.reply_text(zen.text)

# Get random jokes
def laugh(bot, update):
    chat_id = update.message.chat_id
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    headers = {'Accept': 'text/plain'}
    # url = 'https://icanhazdadjoke.com/'
    url = 'http://is.snssdk.com/neihan/stream/mix/v1/?mpic=1&webp=1&essence=1&content_type=-102&message_cursor=-1&am_longitude=110&am_latitude=120&am_city=%E5%8C%97%E4%BA%AC%E5%B8%82&am_loc_time=1489226058493&count=1&min_time=1489205901&screen_width=1450&do00le_col_mode=0&iid=3216590132&device_id=32613520945&ac=wifi&channel=360&aid=7&app_name=joke_essay&version_code=612&version_name=6.1.2&device_platform=android&ssmix=a&device_type=sansung&device_brand=xiaomi&os_api=28&os_version=6.10.1&uuid=326135942187625&openudid=3dg6s95rhg2a3dg5&manifest_version_code=612&resolution=1450*2800&dpi=620&update_version_code=6120'
    joke_json = requests.get(url)
    joke = json.loads(joke_json.text)
    text = joke['data']['data'][0]['group']['content']
    update.message.reply_text(text)

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
        api = auth_twitter()
        api.update_status(status = msg['text'])

    else:
        file = bot.getFile(msg['photo'][-1]['file_id'])
        path = file['file_path']
        # Channel
        bot.send_photo(chat_id=chat_id, photo=msg['photo'][-1]['file_id'], caption=msg['caption'] if 'caption' in msg.keys() else None)
        # print('message_files/pics/' + path.split('/')[-1])
        # Facebook
        graph.put_photo(image=open('message_files/pics/' + path.split('/')[-1], 'rb'), message=msg['caption'] if 'caption' in msg.keys() else 'No caption.')
        # Twitter
        api = auth_twitter()
        api.update_with_media('message_files/pics/' + path.split('/')[-1], status = msg['caption'] if 'caption' in msg.keys() else 'No caption.')

    subprocess.call(['rm', 'message_files', '-rf'])
    subprocess.call(['mkdir', 'message_files'])

def auth_twitter():
    auth = tweepy.OAuthHandler(t_api_key, t_api_sec)
    auth.set_access_token(t_token, t_sec)
    return tweepy.API(auth)
