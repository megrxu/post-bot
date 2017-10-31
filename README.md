# Post Bot

A telegram bot to post moments or activities on multiple platforms.

## Requirements

Python modules:
- facebook-sdk
- python-telegram-bot
- requests

## Usage

Get your Telegram user-id, Channel chat-id, and Facebook access token.

Also, if you want news feature enabled, you will need a news_api appid at [News API](https://newsapi.org/).

Add a file named `ids.py`, just like this:
```python
news_api = 'your_appid'
bot_token = 'your_token'
TyteKa = your_id
TyteKaChannel = your_chat_id
facebook_auth_token = 'your_token'
facebook_id = 'your_user_id'
```

And then:
```sh
python ./bot.py
```

## Features

- Get the news from different sources.
- Random jokes(haha).
- Post news to your channel every day.
- Get the message you sent to it, and then post on your Facebook timeline and in your private channel **when confirmed**.
- Also, echo the message if someone(not you) sent to it.

## Screenshots

(To be added)
