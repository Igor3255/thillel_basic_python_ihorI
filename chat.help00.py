import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Replace YOUR_API_KEY with your own API key
api_key = '6156984959:AAH-C-bbAoeBnsFUXtYZ7aFD7SDFYOsDlco'
bot = telegram.Bot(token=api_key)

# Define a function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm a bot! How can I help you?")

# Define a function to handle text messages
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# Define a function to handle the /help command
def help(update, context):
    help_message = "Here are some commands you can use:\n"
    help_message += "/start - Start the bot\n"
    help_message += "/help - Show this help message\n"
    help_message += "/echo <message> - Repeat the message\n"
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_message)

# Define a function to handle the /echo command
def repeat_message(update, context):
    message = ' '.join(context.args)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# Set up the bot handlers
updater = Updater(api_key, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('echo', repeat_message))
dispatcher.add_handler(MessageHandler(Filters.text, echo))

# Start the bot
updater.start_polling()
