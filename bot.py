import utils, commands, tasks, datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Job, CallbackQueryHandler
from creadcials import *

# Connect to the bot
updater = Updater(bot_token)

# Dispatch and add jobs
updater.dispatcher.add_handler(CommandHandler('hello', commands.hello))
updater.dispatcher.add_handler(CommandHandler('laugh', commands.laugh))
updater.dispatcher.add_handler(CommandHandler('news', commands.news))
updater.dispatcher.add_handler(CommandHandler('hans', commands.hans))
updater.dispatcher.add_handler(CommandHandler('zen', commands.zen))

updater.dispatcher.add_handler(CallbackQueryHandler(utils.callback_dispatcher))
updater.dispatcher.add_handler(MessageHandler(Filters.all, utils.chat_dispatcher))

updater.job_queue.run_daily(tasks.daily_sch, time=datetime.time(0, 0, 0), name='daily')

# Start the bot
updater.start_polling()
updater.idle()
