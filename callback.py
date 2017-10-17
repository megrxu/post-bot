import telegram, requests, json, utils
from ids import *

def go_where(bot, update):
    if (update.callback_query['data'] in 'yn'):
      ifpost(bot, update)
    else:
      send_news(bot, update)

def send_news(bot, update):
    chat_id = update.callback_query.from_user.id
    bot.answer_callback_query(callback_query_id=update.callback_query.id, text='Here you go!')
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    source = update.callback_query['data']
    url = 'https://newsapi.org/v1/articles?source={source}&apiKey={apiKey}'.format(source=source, apiKey=news_api)
    news_json = requests.get(url)
    news_object = json.loads(news_json.text)
    for item in news_object['articles']:
        text = ('*{title}*\n[Link]({link})'.format(title=item['title'], link=item['url']))
        bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.MARKDOWN, disable_web_page_preview=False)
    #   if (item['urlToImage'] != '' and '(' not in item['urlToImage']):
    #     if item['urlToImage'][0] == '/':
    #         url = 'https:' + item['urlToImage']
    #     else:
    #         url = item['urlToImage']
    #     bot.send_photo(chat_id=chat_id, photo=url, reply_to_message_id=k)
    
def ifpost(bot, update):
    chat_id = update.callback_query.from_user.id
    if (update.callback_query['data'] == 'y'):
      bot.answer_callback_query(callback_query_id=update.callback_query.id, text='OK, I\'ll post it for you!')

      file_object = open('message_meta.py', 'r')
      try:
          msg_str = file_object.read()
      finally:
          file_object.close()
      msg = eval(msg_str)
      utils.save_message(bot, msg)

    else:
      bot.answer_callback_query(callback_query_id=update.callback_query.id, text='Canceled.')
    
    # bot.edit_message_reply_markup(chat_id=chat_id, message_id=sent.message_id, reply_markup=None)
