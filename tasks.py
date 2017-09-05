def news_sch(bot, job):
    url = 'https://newsapi.org/v1/articles?source={source}&apiKey={apiKey}'.format(source='google-news', apiKey=news_api)
    news_json = requests.get(url)
    news_object = json.loads(news_json.text)

    for item in news_object['articles']:
      text = '*{title}* \n\n{desp} \n\n[Link]({link}) \n{time}'
      text = text.format(title=item['title'], link=item['url'], desp=item['description'], time=item['publishedAt'])
      chat_id = '@TyteKa_Channel'
      k = bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.MARKDOWN, disable_web_page_preview=True).message_id
      if (item['urlToImage'] != '' and '(' not in item['urlToImage']):
        if item['urlToImage'][0] == '/':
            url = 'https:' + item['urlToImage']
        else:
            url = item['urlToImage']
        bot.send_message(chat_id=chat_id, text='[Image]({link})'.format(link=url), parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=k)