import os
import random
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
commandList = ['help', 'Fact!', 'Add fact', 'Remove fact', 'List facts']

usefulFacts = ['A day has 24 hours in it.', 'A football is round.']


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
        if message.content.startswith('^help'):
            helpMessage = "Here are the available commands:\n"
            for command in commandList:
                helpMessage += f"{command}\n"
            await message.channel.send(helpMessage)

        if message.content.startswith('^Fact!'):
            index = random.randint(0, len(usefulFacts) - 1)
            await message.channel.send(usefulFacts[index])
        if message.content.startswith('^Add fact'):
            if (len(message.content) > len('^Add fact ')):
                msg = message.content[len('^Add fact ') : len(message.content)]
                usefulFacts.append(msg)
        if message.content.startswith('^Remove fact'):
            if (len(message.content) > len('^Add fact ')):
                msg = message.content[len('^Remove fact ') : len(message.content)]
                for fact in usefulFacts:
                    if fact == msg:
                        usefulFacts.remove(fact)
        if message.content.startswith('^List facts'):
            factsMessage = "Facts:\n"
            for fact in usefulFacts:
                factsMessage += f"{fact}\n"
            await message.channel.send(factsMessage)
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