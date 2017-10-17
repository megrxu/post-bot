from ids import *
import telegram, requests, json

# Runs 8:00 every day
def news_sch(bot, job):
    url = 'https://newsapi.org/v1/articles?source={source}&apiKey={apiKey}'.format(source='engadget', apiKey=news_api)
    news_json = requests.get(url)
    news_object = json.loads(news_json.text)

    # chat_id = '@TyteKa_Channel'
    chat_id = -1001103536115
    bot.send_message(chat_id=chat_id, text='Good morning!')
    text = '*Engadget at Today\'s 8:00*  #news\n\n'
    text += '-------------------\n'
    for item in news_object['articles']:
        text += ('{title}\n[Link]({link})\n'.format(title=item['title'], link=item['url']))
        text += '-------------------\n'
    bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.MARKDOWN, disable_web_page_preview=True)
