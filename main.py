import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='r!')

@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "ratio" in message.content.lower:
        upvote = '⬆'
        downvote = '⬇'
        print("Message '{0.content}' contains word 'ratio'.".format(message))
        await message.add_reaction(upvote)
        await message.add_reaction(downvote)

def main():
    print("Please input bot token.")
    bot.run(input())

main()
