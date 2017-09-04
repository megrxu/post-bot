from telegram.ext import Updater, CommandHandler
import requests, json
import telegram
from apiKeys import *

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

# Get random jokes
def laugh(bot, update):
    headers = {'Accept': 'text/plain'}
    joke = requests.get('https://icanhazdadjoke.com/',headers=headers)
    update.message.reply_text(joke.text)

def news(bot, update):
    news_json = requests.get('https://newsapi.org/v1/articles?source=techcrunch&apiKey=' + news_api)
    news_json = news_json.text
    news_object = json.loads(news_json)
    for item in news_object['articles']:
      text = '*{title}* \n\n{desp} \n\n[Link]({link}) \n{time}'
      text = text.format(title=item['title'], link=item['url'], desp=item['description'], time=item['publishedAt'])
      chat_id = update.message.chat_id
    #   chat_id = '@TyteKa_Channel'
      k = bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.MARKDOWN, disable_web_page_preview=True).message_id
      if (item['urlToImage'] != '' and '(' not in item['urlToImage']):
        if item['urlToImage'][0] == '/':
            url = 'https:' + item['urlToImage']
        else:
            url = item['urlToImage']
        bot.send_message(chat_id=chat_id, text='[Image]({link})'.format(link=url), parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=k)
    # bot.send_message(chat_id='@TyteKa_Channel', text='[Image]({link})'.format(link=url), parse_mode=telegram.ParseMode.MARKDOWN)

updater = Updater(bot_token)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('laugh', laugh))
updater.dispatcher.add_handler(CommandHandler('news', news))

updater.start_polling()
updater.idle()
