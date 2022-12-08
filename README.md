# About the BOT

The Nasdaq Bot tracks 10 of the top companies in the Tech and Auto industry each, which are listed on the Nasdaq Stock Exchange. The data is of realtime with a maximum of a 15minute delay in the worst case possible.
Use the $help command to navigate through the commands required to invoke the functionalities of the bot.

```c
$info : To list the companies and respective NASDAQ symbols available for tracking

track {symbol} : To list stock details of the corresponding company

$positive : To list the companies with a positive change percentage

$negative : To list the companies with a negative change percentage

$volume high : To list the company with the largest average volume of stocks traded

$volume low : To list the company with the lowest average volume of stocks traded
```

The following video shows the bot at work and the results of the above commands:

https://user-images.githubusercontent.com/102587700/206395465-ab38b79f-9780-4573-a9b5-61bcb174a353.mp4




# Libraries used

### Financial data:

All the financial data was retreived using the **API** provided by **IEX Cloud.** To access the API, the python library pyEX was used which retrieves data for a company in the form of key value pairs.

Below is an example of the python code used to get the stock data for Apple:

```c
import pyEX as p

c = p.Client(api_token='priv', version='stable') // priv stands for the api token
d = c.quote(symbol='AAPL')
print(d)
```

The following is the output we get:

```c
{'avgTotalVolume': 74955390, 'calculationPrice': 'close', 'change': -1.97, 'changePercent': -0.01378, 'close': 140.94, 'closeSource': 'official', 'closeTime': 1670446800596, 'companyName': 'Apple Inc', 'currency': 'USD', 'delayedPrice': 141.06, 'delayedPriceTime': 1670446783153, 'extendedChange': -0.21, 'extendedChangePercent': -0.00149, 'extendedPrice': 140.73, 'extendedPriceTime': 1670461198364, 'high': 143.37, 'highSource': '15 minute delayed price', 'highTime': 1670446799899, 'iexAskPrice': 0, 'iexAskSize': 0, 'iexBidPrice': 0, 'iexBidSize': 0, 'iexClose': 140.93, 'iexCloseTime': 1670446799748, 'iexLastUpdated': 1670446862225, 'iexMarketPercent': 0.014706797343139797, 'iexOpen': 142.35, 'iexOpenTime': 1670423400404, 'iexRealtimePrice': 141, 'iexRealtimeSize': 100, 'iexVolume': 1025374, 'lastTradeTime': 1670446825141, 'latestPrice': 140.94, 'latestSource': 'Close', 'latestTime': 'December 7, 2022', 'latestUpdate': 1670446800596, 'latestVolume': 69721094, 'low': 140, 'lowSource': '15 minute delayed price', 'lowTime': 1670444522687, 'marketCap': 2242090150920, 'oddLotDelayedPrice': 141.075, 'oddLotDelayedPriceTime': 1670446783804, 'open': 142.28, 'openTime': 1670423400646, 'openSource': 'official', 'peRatio': 23.07, 'previousClose': 142.91, 'previousVolume': 64727186, 'primaryExchange': 'NASDAQ', 'symbol': 'AAPL', 'volume': 69721094, 'week52High': 181.88, 'week52Low': 128.65, 'ytdChange': -0.2042998322924302, 'isUSMarketOpen': False}
```

All the commands revolve around the above data for each company with suitable manipulations done to different values to derive meaningful results.

### Discord connection:

The second library used was the **discord** library.

This facilitates the connection to discord as a client and allows us to write code that revolves around **events : “**an event occurs and an action is taken for it”.

Below is a simple function to demonstrate the concept of events where: a message is sent on the channel, bot checks if it was sent by the user and not itself, bot replies with “Hello” if the message was “Hello”.

```c

intents = discord.Intents().all()
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '$hello':
        await message.channel.send('Hello!')
```

# Code Logic

A data structure called ‘companies’ contains the symbols for all the companies and the following is done for every command:

- track {symbol} - check if the symbol exists, if not then print an error message, else retrieve data and print appropriate fields.
- $positive: iterate through data for each symbol/company and print those with a positive changePercentage field.
- $negative: iterate through data for each symbol/company and print those with a negative changePercentage field.
- $volume high: iterate through data for each symbol/company and print the company with the largest avgVolume field.
- $volume low: iterate through data for each symbol/company and print the company with the lowest avgVolume field.

# Future plans

1. At the moment, the bot is active as long as the python script runs. But as soon as the program stops, the bot goes offline. To resolve this, I’m planning on hosting the bot on a server so the script can run at all times and everyone can use the bot.
2. I will add more functionalities to the bot as more ideas strike me.
