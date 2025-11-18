import os

import discord

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
#set the intents so that the Bot can acess
# message Content of users

intents = discord.Intents.default()
intents.message_content = True
#pass the intents into the client 
client = discord.Client(intents =intents)

#the list of commands without prefix "^". "^" is needed to get the bot to respond
commandList = ['help', 'hello', 'do something']



#"@" is a decorator to regiseter an event that
#the client will listen to
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('^'):
        await message.channel.send('Hello!')
        if message.content.startswith('^help'):
            helpMessage = "Here are the available commands:\n"
            for command in commandList:
                helpMessage += f"{command}\n"
            await message.channel.send(helpMessage)

#print the error message when an error occurs
@client.event
async def on_error(error):
    print(f'Error: {error}')

@client.event
async def on_guild_join(guild):
    print(f'Joined guild: {guild.name} (id: {guild.id})')

@client.event
async def on_guild_emojis_update(guild, emojiSetBefore, emojiSetAfter):
    for emojiAfter in emojiSetAfter:
        if emojiAfter not in emojiSetBefore:
            print(f'New emoji added: {emojiAfter.name} in guild: {guild.name}')
    for emojiBefore in emojiSetBefore:
        if emojiBefore not in emojiSetAfter:
            print(f'Emoji removed: {emojiBefore.name} in guild: {guild.name}')
client.run(TOKEN)