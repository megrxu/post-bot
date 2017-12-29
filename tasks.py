from ids import *
import telegram, requests, json
from utils import randomCN

# Runs 8:00 every day
def news_sch(bot, job):
    url = 'https://newsapi.org/v1/articles?source={source}&apiKey={apiKey}'.format(source='engadget', apiKey=news_api)
    news_json = requests.get(url)
    news_object = json.loads(news_json.text)

    chat_id = TyteKaChannel
    bot.send_message(chat_id=chat_id, text='Good morning!')
    text = '*Engadget at Today\'s 8:00*  #news\n\n'
    text += '-------------------\n'
    for item in news_object['articles']:
        text += ('{title}\n[Link]({link})\n'.format(title=item['title'], link=item['url']))
        text += '-------------------\n'
    bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.MARKDOWN, disable_web_page_preview=True)

def laugh_sch(bot, job):
    headers = {'Accept': 'text/plain'}
    # url = 'https://icanhazdadjoke.com/'
    url = 'http://is.snssdk.com/neihan/stream/mix/v1/?mpic=1&webp=1&essence=1&content_type=-102&message_cursor=-1&am_longitude=110&am_latitude=120&am_city=%E5%8C%97%E4%BA%AC%E5%B8%82&am_loc_time=1489226058493&count=1&min_time=1489205901&screen_width=1450&do00le_col_mode=0&iid=3216590132&device_id=32613520945&ac=wifi&channel=360&aid=7&app_name=joke_essay&version_code=612&version_name=6.1.2&device_platform=android&ssmix=a&device_type=sansung&device_brand=xiaomi&os_api=28&os_version=6.10.1&uuid=326135942187625&openudid=3dg6s95rhg2a3dg5&manifest_version_code=612&resolution=1450*2800&dpi=620&update_version_code=6120'
    joke_json = requests.get(url)
    joke = json.loads(joke_json.text)
    text = joke['data']['data'][0]['group']['content']
    chat_id = TyteKaChannel
    text = 'Good morning!\n----------------\n*Today\'s joke:*  #jokes\n\n{joke}'.format(joke = text)
    bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.MARKDOWN)

def zen_sch(bot, job):
    zen = requests.get('https://api.github.com/zen')

    chat_id = TyteKaChannel
    text = 'Good morning!\n*{zen}*\n#zen'.format(zen = zen.text)
    bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.MARKDOWN)

def hans_sch(bot, job):
    text = randomCN()
    chat_id = TyteKaChannel
    text = 'Good morning!\n*{zen}*'.format(zen = text)
    bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.MARKDOWN)

def daily_sch(bot, job):
    laugh_sch(bot, job)