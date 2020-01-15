import discord

client = discord.Client()

import random as r

def War(oneElite, oneNorm, twoElite, twoNorm):
    
    final = 0
    score1 = 0
    score2 = 0
    for i in range(oneElite):
        score1 += r.randint(0,6)
    for i in range(oneNorm):
        score1 += r.randint(0,4)
    for i in range(twoElite):
        score2 += r.randint(0,6)
    for i in range(twoNorm):
        score2 += r.randint(0,4)
    fianl = score1 - score2
    if final == 0:
        return ('tie! team 1 and 2 score{}'.format(score1, score2))
    elif fianl > 0:
        return ('team 1 wins! team 1 score {}, team 2 score{}'.format(score1, score2))
    else: #score < 0
        return ('team 2 wins! team 1 score {}, team 2 score{}'.format(score1, score2))
    
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('StartWar'):
        await message.channel.send('input number of team 1 elites')
        print('1 elites')
        @client.event
        async def on_message(message):
            if message.author == client.user:
                return
            else:
                oneElite = int(message.content)
                await message.channel.send('input number of team 1 normals')
                print('1 norms')
                print('check 1')
                @client.event
                async def on_message(message):
                    if message.author == client.user:
                        return
                    else:
                        oneNorm = int(message.content)
                        await message.channel.send('input number of team 2 elites')
                        print('2 elites')
                        print('check 2')
                        @client.event
                        async def on_message(message):
                            if message.author == client.user:
                                return
                            else:
                                twoElite = int(message.content)
                                await message.channel.send('input number of team 2 normals')
                                print('2 norms')
                                print('check 3')
                                @client.event
                                async def on_message(message):
                                    if message.author == client.user:
                                        return
                                    else:
                                        twoNorm = int(message.content)
                                        results = War(oneElite, oneNorm, twoElite, twoNorm)
                                        await message.channel.send(results)
                                
                

                
client.run('NjY0MTk4MTEzNzc4NzI4OTgw.XhVUHQ.s-6HT8FOp88D5GtXcb3hm7CIODM')
