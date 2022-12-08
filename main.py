import discord
import pyEX as p

c = p.Client(api_token='priv', version='stable')
d = c.quote(symbol='SSNLF')
print(d)

companies = [
    'AAPL', 'MSFT', 'AMZN', 'GOOGL', 'SSNLF', 'TM', 'DDAIF', 'TSLA', 'BAMXF',
    'CSCO', 'META', 'IBM', 'SAP', 'INTC', 'STLA', 'RIVN', 'LI', 'MULN', 'VLCN',
    'PCAR'
]

intents = discord.Intents().all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    text = message.content
    if message.author == client.user:
        return

    if message.content == '$hello':
        await message.channel.send('Hello!')

    if message.content == '$info':
        await message.channel.send(
            'Tech companies:\n1.Apple - AAPL\n2.Microsoft - MSFT\n3.Amazon - AMZN\n4.Google - GOOGL\n5.Samsung - SSNLF\n6.Meta - META\n7.IBM - IBM\n8.SAP SE - SAP\n9.Intel - INTC\n10.Cisco - CSCO\n\nAuto Companies:\n1.Toyota Motors - TM\n2.Mercedes Benz - DDAIF\n3.Tesla - TSLA\n4.BMW - BAMXF\n5.Stellantis - STLA\n6.Rivian - RIVIN\n7.Li Auto - LI\n8.Mullen Technologies - MULN\n9.Volcon INC - VLCN\n10.Paccar - PCAR'
        )

    if message.content == '$help':
        await message.channel.send(
            '$info : To list the companies and respective NASDAQ symbols available for tracking\n\n${symbol} : To list trading details of the company co\n\n$positive : To list the companies with a positive change percentage\n\n$negative : To list the companies with a negative change percentage'
        )

    if 'track' in text:
        words = text.split(' ')
        if (len(words) == 2):
            if (words[1] in companies):
                data = c.quote(symbol=words[1])
                await message.channel.send('Company Name: ' + data['companyName'] +
                                           '\nPrevious Day Closing Price: ' +
                                           str(data['previousClose']) + ' USD\n' +
                                           'Latest Price: ' +
                                           str(data['latestPrice']) + ' USD\n' +
                                           '52 Week High: ' + str(data['week52High']) +
                                           ' USD\n' + '52 Week Low' +
                                           str(data['week52Low']) + ' USD\n')
            else:
                await message.channel.send(
                    'Use the info command to refer to the list of available companies')

    if message.content == '$positive':
        positive = ''
        for i in range(len(companies)):
            print(i)
            print(companies[i])
            data = c.quote(symbol=companies[i])
            print(data)
            if (data['changePercent'] > 0):
                positive += (data['companyName'] + ' : ' + str(data['changePercent']) +
                             '\n')
                print('found')

        await message.channel.send(positive)

    if message.content == '$negative':
        negative = ''
        for i in companies:
            data = c.quote(symbol=i)
            if (data['changePercent'] < 0):
                negative += (data['companyName'] + ' : ' + str(data['changePercent']) +
                             '\n')

        await message.channel.send(negative)

    if message.content == '$volume high':
        highest = 0
        company = ''
        for i in companies:
            data = c.quote(symbol=i)
            if (data['avgTotalVolume'] > highest):
                highest = data['avgTotalVolume']
                company = i

        await message.channel.send(company + ' : ' + str(highest))

    if message.content == '$volume low':
        lowest = 9999999999999999999999999999999999999999999999
        company = ''
        for i in companies:
            data = c.quote(symbol=i)
            if (data['avgTotalVolume'] < lowest):
                lowest = data['avgTotalVolume']
                company = i

        await message.channel.send(company + ' : ' + str(lowest))


client.run(
    'priv')
