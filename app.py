import discord
import os

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        

    # if message.content.startswith('deneme'):
    #     await message.channel.send('deneme')



    if 'atakan' in message.content :
        emote ='\U0001F923'
        await message.add_reaction(emote)    

    if '<@819914389120352277>' in message.content :
        emote ='\U0001F923'
        await message.add_reaction(emote)    
    
            
          

@client.event
async def on_message_edit (before, after):
    await before.channel.send(
f'{before.author} mesajı editledi \n'
f'Before: {before.content} \n'
f'After: {after.content}'
)


 


client.run(DISCORD_TOKEN)