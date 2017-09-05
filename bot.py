import logging, datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Job
from ids import *
from commands import *
from chat import *
from tasks import *


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(bot_token)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('laugh', laugh))
updater.dispatcher.add_handler(CommandHandler('news', news))
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
updater.job_queue.run_daily(news_sch, time=datetime.time(8, 0, 0), name='News')

updater.start_polling()
updater.idle()
