import asyncio
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()

#client = discord.Client()
bot = commands.Bot(command_prefix='!')



#@client.event
@bot.event
async def on_ready():
    print('We have logged in as {}'.format(bot.user))

#@client.event
@bot.command(name="start", help="Starts a Pomodoro timer")
async def start_timer(ctx):
    start_work_em = discord.Embed(title="Time to start working!", color=0x33c633)
    await ctx.send(embed = start_work_em)
    await asyncio.sleep(5)
    start_play_em = discord.Embed(title="Time to start your break!", color=0x33c633)
    await ctx.send(embed = start_play_em)


@bot.command(name="stop", help="Stop a Pomodoro timer")
async def stop_timer(ctx):
    stop_timer_em = discord.Embed(title="Timer has been stopped!", color=0xc63333)
    await ctx.send(embed = stop_timer_em)



#    if message.author == client.user:
#        return
#    if message.content.startswith('$hello'):
#        await message.channel.send('Hello!')


#client.run(os.environ['BOT_TOKEN'])
bot.run(os.environ['BOT_TOKEN'])

