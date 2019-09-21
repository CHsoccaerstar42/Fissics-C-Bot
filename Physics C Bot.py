import discord
import os
from datetime import date
from discord.ext import commands


client = commands.Bot(command_prefix = '.')

@client.event

async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    user = str(message.author)
    if user == 'B Team Bot#7552':
        return
    user = user[:-5]
    sentence_string = message.content
    sentence_list = sentence_string.split()
    if sentence_string == 'date':
        today = date.today()
        year = today.year
        month = today.month
        day = today.day

        if month == 4:
            day += 31
            month -= 1
        if month == 3:
            day += 28
            month -= 1
        if month == 2:
            day += 31
            month -= 1
        if month == 1:
            day += 31
            month = 12
            year -= 1
        if month == 12:
            day += 30
            month -= 1
        if month == 11:
            day += 31
            month -= 1
        if month == 10:
            day += 30
            month -= 1
        if month == 9:
            day += 31
            month -= 1
        if month == 8:
            day += 31
            month -= 1
        if month == 7:
            day += 31
            month -= 1
        if month == 6:
            day += 30
            month -= 1
            
        while year > 2018:
            day += 365
            if year % 4 == 0:
                day += 1
            year -= 1
        if day % 10 == 1:
            await message.channel.send('May the ' + str(day) + 'st be with you!')
        elif day % 10 == 1:
            await message.channel.send('May the ' + str(day) + 'nd be with you!')
        elif day % 10 == 1:
            await message.channel.send('May the ' + str(day) + 'rd be with you!')
        else:
            await message.channel.send('May the ' + str(day) + 'th be with you!')
    if 'istylerdum' in message.content.lower():
        await message.channel.send('TylerIsDum = True')


@client.command(aliases=['ISTYLERDUM', 'istylerdum', 'IsTylerDum'])
async def isTylerDum(ctx):
    await ctx.send('TylerIsDum = True')

client.run('NjI0ODE0NjA2NTUyMDA2NzE5.XYWeCw.j8OhywqZsSH_md10sqeiwFHCe0c')
