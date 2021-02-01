import asyncio
import discord
import os
from timer import Timer
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

bot = commands.Bot(command_prefix='!', help_command=None)
timer = Timer()


@bot.event
async def on_ready():
    print('We have logged in as {}'.format(bot.user))


@bot.command(name="start", help="Starts a Pomodoro timer")
async def start_timer(ctx):
    start_work_em = discord.Embed(title="Time to start working!", color=0x33c633)
    await ctx.send(embed=start_work_em)
    timer.start()
    while timer.is_running():
        await asyncio.sleep(1)
        timer.tick()
        if timer.get_ticks() >= 10:
            timer.stop()
    start_play_em = discord.Embed(title="Time to start your break!", color=0x33c633)
    await ctx.send(embed=start_play_em)


@bot.command(name="stop", help="Stop a Pomodoro timer")
async def stop_timer(ctx):
    stop_timer_em = discord.Embed(title="Timer has been stopped!", color=0xc63333)
    await ctx.send(embed=stop_timer_em)
    timer.stop()


@bot.command(name="time", help="Show current time")
async def show_time(ctx):
    await ctx.send(f"Current timer status is : {timer.is_running()}")
    await ctx.send(f"Current time is : {timer.get_ticks()}")


@bot.command(name="help", help="Show help text")
async def show_help(ctx):
    help_commands = dict()
    for command in bot.commands:
        help_commands[command.name] = command.help
    description = "Bot commands are: {}".format(help_commands)
    show_help_em = discord.Embed(title="This is Mr Pomo Dorio, a friendly Pomodoro bot", description=description,
                                 color=0xc63333)
    await ctx.send(embed=show_help_em)


bot.run(os.environ['BOT_TOKEN'])
