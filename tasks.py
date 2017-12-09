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
    joke = requests.get('https://icanhazdadjoke.com/',headers=headers)
    chat_id = TyteKaChannel
    text = 'Good morning!\n----------------\n*Today\'s joke:*  #jokes\n\n{joke}'.format(joke = joke.text)
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