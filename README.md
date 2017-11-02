# Post Bot

A telegram bot to post moments or activities on multiple platforms.

## Requirements

Python modules:
- facebook-sdk
- python-telegram-bot
- tweepy
- requests

## Usage

Get your Telegram user-id, Channel chat-id, and Facebook access token.

Also, if you want news feature enabled, you will need a news_api appid at [News API](https://newsapi.org/).

Add a file named `ids.py`, just like this:
```python
# News API
news_api = 'your_appid'

# Telegram
bot_token = 'your_token'
TyteKa = your_id
TyteKaChannel = your_chat_id

# Facebook
facebook_auth_token = 'your_token'
facebook_id = 'your_user_id'

# Twitter
t_api_key = 'your_app_key'
t_api_sec = 'your_app_sec'
t_token = 'your_access_token'
t_sec = 'access_sec'
```

And then:
```sh
python ./bot.py
```

## Features

- Get the news from different sources.
- Random jokes(haha).
- Post news to your channel every day.
- Get the message you sent to it, and then post on your Facebook timeline , in your private channel and on Twitter **when confirmed**.
- Also, echo the message if someone(not you) sent to it.

## Screenshots

(To be added)
