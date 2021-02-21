import asyncio
import discord
import os
from pomobot.timer import Timer, TimerStatus
from dotenv import load_dotenv
from discord.ext import commands

COLOR_DANGER = 0xc63333
COLOR_SUCCESS = 0x33c633



class DiscordCog(commands.Cog):


    def __init__(self, bot):
        self.bot = bot
        self.timer = Timer()


    @commands.Cog.listener()
    async def on_ready(self):
        print('We have logged in as {}'.format(self.bot.user))


    @commands.command()
    async def start(self, ctx):
        if self.timer.get_status() == TimerStatus.RUNNING:
            await self.show_message(ctx, "Timer is already running! You should stop the timer before you can restart it!", COLOR_SUCCESS)    
            return
        await self.show_message(ctx, "Time to start working!", COLOR_SUCCESS)
        self.timer.start(max_ticks=10)
        while self.timer.get_status() == TimerStatus.RUNNING:
            await asyncio.sleep(1)
            self.timer.tick()
        if self.timer.get_status() == TimerStatus.EXPIRED:
            await self.show_message(ctx, "Time to start your break!", COLOR_SUCCESS)
            self.timer.start(max_ticks=10)
            while self.timer.get_status() == TimerStatus.RUNNING:
                await asyncio.sleep(1)
                self.timer.tick()
            if self.timer.get_status() == TimerStatus.EXPIRED:
                await self.show_message(ctx, "Okay, break over!", COLOR_SUCCESS)


    async def show_message(self, ctx, title, color):
        start_work_em = discord.Embed(title=title, color=color)
        await ctx.send(embed=start_work_em)


    @commands.command()
    async def stop(self, ctx):
        if self.timer.get_status() != TimerStatus.RUNNING:
            await self.show_message(ctx, "Timer is already stopped! You should start the timer before you can stop it!", COLOR_SUCCESS)    
            return        
        await self.show_message(ctx, "Timer has been stopped!", COLOR_DANGER)
        self.timer.stop()


    @commands.command()
    async def show_time(self, ctx):
        await ctx.send(f"Current timer status is : {self.timer.get_status()}")
        await ctx.send(f"Current time is : {self.timer.get_ticks()}")


    @commands.command()
    async def show_help(self, ctx):
        help_commands = dict()
        for command in self.bot.commands:
            help_commands[command.name] = command.help
        description = "Bot commands are: {}".format(help_commands)
        show_help_em = discord.Embed(title="This is Mr Pomo Dorio, a friendly Pomodoro bot", description=description,
                                    color=COLOR_SUCCESS)
        await ctx.send(embed=show_help_em)






