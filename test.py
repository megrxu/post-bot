import requests, json

news_json = requests.get('https://newsapi.org/v1/sources?language=en')
news_json = news_json.text
print(news_json)
news_object = json.loads(news_json)
print(news_json)
for item in news_object['sources']:
  print(item['url'])