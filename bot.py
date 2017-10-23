import utils, commands, tasks, datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Job, CallbackQueryHandler
from ids import *

# Connect to the bot
updater = Updater(bot_token)

# Dispatch and add jobs
updater.dispatcher.add_handler(CommandHandler('hello', commands.hello))
updater.dispatcher.add_handler(CommandHandler('laugh', commands.laugh))
updater.dispatcher.add_handler(CommandHandler('news', commands.news))

updater.dispatcher.add_handler(CallbackQueryHandler(utils.callback_dispatcher))
updater.dispatcher.add_handler(MessageHandler(Filters.all, utils.chat_dispatcher))

updater.job_queue.run_daily(tasks.news_sch, time=datetime.time(0, 0, 0), name='News')

# Start the bot
updater.start_polling()
updater.idle()
