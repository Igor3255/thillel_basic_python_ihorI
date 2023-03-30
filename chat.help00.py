import requests
import telegram
import ccxt
from apscheduler.schedulers.background import BackgroundScheduler
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Replace YOUR_API_KEY with your own API key
api_key = '6156984959:AAH-C-bbAoeBnsFUXtYZ7aFD7SDFYOsDlco'
bot = telegram.Bot(token=api_key)


def start(update, context):
    # Create an inline keyboard with cryptocurrency buttons
    keyboard = [
        [
            InlineKeyboardButton("Bitcoin", callback_data='BTC'),
            InlineKeyboardButton("Ethereum", callback_data='ETH')
        ],
        [
            InlineKeyboardButton("Litecoin", callback_data='LTC'),
            InlineKeyboardButton("Dogecoin", callback_data='DOGE')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите криптовалюту:', reply_markup=reply_markup)


# создание экземпляра класса Updater
updater = Updater(api_key, use_context=True)

# получение диспетчера (dispatcher) у экземпляра класса Updater
dispatcher = updater.dispatcher


def button(update, context):
    query = update.callback_query
    symbol = query.data

    # Get the price of the symbol using ccxt library
    exchange = ccxt.binance()
    ticker = exchange.fetch_ticker(symbol)
    price = ticker['last']

    # Send the price as a message to the user
    message = f"The current price of {symbol} is {price:.8f} USDT"
    context.bot.send_message(chat_id=query.message.chat_id, text=message)


InlineKeyboardButton("Bitcoin", callback_data='BTC')
InlineKeyboardButton("Ethereum", callback_data='ETH')
InlineKeyboardButton("Litecoin", callback_data='LTC')
InlineKeyboardButton("Dogecoin", callback_data='DOGE')

updater.dispatcher.add_handler(CallbackQueryHandler(button))


def crypto_price(update, context):
    query = update.callback_query
    symbol = query.data

    # Connect to the exchange using the API key
    exchange = ccxt.binance({
        'apiKey': 'hVY0C2u30Q9HZww7g6v1qZC9J8dYoCNs5pz0h7n88IFjIGSeNZ5CQGwGWkBIQRNL',
        'secret': 'tlDnv4m7YyQQt4TKR1Mhk94v7jAzKAESroM5U2jqgVxdo2xLP59zppWqt9zrXERx',
        'enableRateLimit': True,
    })

    # Get the latest price for the selected cryptocurrency
    ticker = exchange.fetch_ticker(symbol + 'LUNC/USDT')
    price = ticker['last']

    # Send the price to the user
    query.edit_message_text(text="The current price of {} is {} USDT".format(symbol, price))


# Define a function to handle the callback from the inline keyboard
def crypto_price(update, context):
    query = update.callback_query
    symbol = query.data
    exchange = ccxt.binance()
    ticker = exchange.fetch_ticker(symbol)
    price = ticker['last']
    context.bot.send_message(chat_id=query.message.chat_id, text=f"Цена {symbol}: {price}")


# Define a function to handle the /help command
def help(update, context):
    help_message = "Here are some commands you can use:\n"
    help_message += "/start - Start the bot\n"
    help_message += "/help - Show this help message\n"
    help_message += "/price - Show the current Bitcoin price in USD\n"
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_message)


# Set up the bot handlers
updater = Updater(api_key, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))


def list_commands(update, context):
    command_list = ["/start - Start the bot",
                    "/help - Show this help message"]
    context.bot.send_message(chat_id=update.effective_chat.id, text="\n".join(command_list))


# Add the /help command to the dispatcher
dispatcher.add_handler(CommandHandler('help', list_commands))


# Define a function to handle the /price command
def get_price(update, context):
    # Get the current Bitcoin price in USD from Binance API
    url = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
    response = requests.get(url)
    price = response.json()['price']

    # Send the price to the user
    message = f"The current Bitcoin price is ${price}"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


# Define a function to update the Bitcoin price every 5 minutes
def update_price():
    api_key = "YOUR_API_KEY_HERE"
    url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}&symbols=EUR,USD"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        usd_rate = data["rates"]["USD"]
        eur_rate = data["rates"]["EUR"]
        return (usd_rate, eur_rate)
    else:
        print("Failed to update price")


# Set up the bot handlers
updater = Updater(api_key, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('price', get_price))
dispatcher.add_handler(telegram.ext.CallbackQueryHandler(button))

# Set up the price update scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(update_price, 'interval', minutes=5)
scheduler.start()

# Start the bot
updater.start_polling()
