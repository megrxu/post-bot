import logging, datetime, commands, chat, tasks, callback
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Job, CallbackQueryHandler
from ids import *

# log
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Connect to the bot
updater = Updater(bot_token)

# Dispatch and add jobs
updater.dispatcher.add_handler(CommandHandler('hello', commands.hello))
updater.dispatcher.add_handler(CommandHandler('laugh', commands.laugh))
updater.dispatcher.add_handler(CommandHandler('news', commands.news))
updater.dispatcher.add_handler(CallbackQueryHandler(callback.go_where))
updater.dispatcher.add_handler(MessageHandler(Filters.all, chat.check))

updater.job_queue.run_daily(tasks.news_sch, time=datetime.time(0, 5, 0), name='News')

# Start the bot
updater.start_polling()
updater.idle()
