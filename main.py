import discord
from datetime import date
from discord.ext import commands
from webserver import keep_alive
import os
import sys
import asyncio
import datetime
import youtube_dl
from random import randint as rand
from discord.ext.commands import has_permissions

ChristianServer = True

client = commands.Bot(command_prefix='.')

counter = 0

players = {}
'''
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def nothing(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)
'''
@client.command()
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
async def Christian(ctx, arg):
	global ChristianServer
	if arg.lower() == 'true':
		ChristianServer = True
		await ctx.channel.send('This is now a christian discord server')
	else:
		ChristianServer = False
		await ctx.channel.send('This is no longer a christian discord server')
@client.event
async def on_message(message):
	global ChristianServer
	global counter
	channel = str(message.channel)
	user = str(message.author)
	nick = str(message.author.nick)
	if user == 'B Team Bot#7552':
		return
	user = user[:-5]
	sentence_string = message.content.lower()
	sentence_list = sentence_string.split()
	sentence1_list = message.content.split()
	nono = False

	if str(message.channel).lower() == 'jeb':
		if message.content.lower() != 'jeb' and user != 'Fissics C Bot':
			await message.channel.send("You fool. you absolute buffoon. you think you can challenge me in my own realm? you think you can rebel against my authority? you dare come into my house and upturn my dining chairs and spill coffee grounds in my Keurig? you thought you were safe in your chain mail armor behind that screen of yours. I will take these laminate wood floor boards and destroy you. I didn't want a war, but I didn't start it.")
			await message.channel.send(file=discord.File('./Images/coolBugFacts.jpg'))
			await message.channel.send(file=discord.File('./Images/youFool.jpg'))

	if user == 'AlG':
		alex = rand(1, 200)
		print(alex)
		if alex == 69:
			await message.channel.send('Did you mean to search for femur breaker?')
			await message.channel.send('https://www.youtube.com/watch?v=08L9sNuik5M')
	'''
  ##### COME BACK TO THIS
	if user == 'CHsoccaerstar42':
		rAnDoMnUmBeR = rand(1, 5)
		print(rAnDoMnUmBeR)
		if rAnDoMnUmBeR == 5:
			channel = message.author.voice.channel
			await channel.connect()
			await message.channel.send('!p femur breaker')
  '''

	if ("im" in sentence_list or "i'm" in sentence_list or 'i’m' in sentence_list) and user != 'Fissics C Bot' and sentence_list[-1] != 'im' and (sentence_list[-1] != "i'm" or sentence_list[-1] != 'im' or sentence_string != 'i’m'):
		run = False
		maydad = ''
		for i in sentence1_list:
			if run:
				maydad += i
				maydad += ' '
			elif i.lower() == 'im' or i.lower() == "i'm" or i.lower() == 'i’m':
				run = True
		await message.channel.send('Hi ' + maydad +
			                           "I'm May")
                                 

	if sentence_string == 'profile':
		await client.edit(avatar='profilePic.jpg')

	if sentence_string == 'date':
		today = date.today()
		year = today.year
		month = today.month
		day = today.day
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
		# if month == 5:
		#  day += 31
		#  month -= 1

		while year > 2018:
			day += 365
			if year % 4 == 0:
				day += 1
			year -= 1
		if day % 100 == 13:
			await message.channel.send('May the ' + str(day) +
			                           'rd be with you!')
		elif day % 10 == 3:
			await message.channel.send('May the ' + str(day) +
			                           'th be with you!')
		else:
			await message.channel.send('May the ' + str(day) +
			                           'rd be with you!')
		currentDT = datetime.datetime.now()


#      if date.today().weekday() == 1 and counter == 0:
#          counter = 1
#      elif date.today().weekday() == 1 and counter == 1:
#          print('Reginald has arrived')
#          counter = 0
#      else:
#        days_until_he_comes = 0
#        if counter == 0:
#          days_until_he_comes = 7
#        day1 = date.today().weekday()
#        days1 = 0
#        while 1 < day1:
#          days1 += 1
#          day1 -= 1
#        days_until_he_comes = days_until_he_comes + (7 - days1)
#        if day1 == 0:
#          days_until_he_comes += 6
#        message1 = 'Reginald will arrive in '+str(days_until_he_comes) + ' days'
#        await message.channel.send(message1)

	if 'istylerdum' == message.content.lower():
		await message.channel.send('TylerIsDum = True')
	if 'columbiainvy' == message.content.lower():
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
			# if month == 5:
			#  day += 31
			#  month -= 1

		while year > 2018:
			day += 365
			if year % 4 == 0:
				day += 1
			year -= 1
		days_until_invy = str(614 - day)
		await message.channel.send('Columbia Invy is in ' + days_until_invy +
		                           ' days')
	if 'reginald' == message.content.lower():
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
			# if month == 5:
			#  day += 31
			#  month -= 1

		while year > 2018:
			day += 365
			if year % 4 == 0:
				day += 1
			year -= 1

		currentDT = datetime.datetime.now()
		days_until_he_comes = 0
		if int(day) % 14 != 1:
			days_until_he_comes = 15 - (day % 14)
			if days_until_he_comes == 15:
				days_until_he_comes = 1
			print('Reginald will arrive in ' + str(days_until_he_comes) +
			      ' days')
			message1 = 'Reginald will arrive in ' + str(
			    days_until_he_comes) + ' days'
			await message.channel.send(message1)
		else:
			print('Reginald has arrived')
			message1 = 'Reginald is arrived'
			await message.channel.send(message1)
			await message.channel.send(file=discord.File('./Images/Reginald.jpeg'))
    

	if 'help' == message.content.lower():
		await message.channel.send('Reginald: Says number of days until a Reginald day' + '\n' +
		    'Date: Gives the date in terms of May 2018' + '\n' +
		    'Istylerdum: Try it' + '\n' +
		    'Columbiainvy: Returns the number of days until the columbia science olympiad invitational'
		    + '\n' + 'Help: Lists all commands I know' + '\n' +
		    'Jeb Wins: Displays our lord and savoir Jeb Bush winning America' +
		    '\n' +
		    'Jeb Wins France: Displays our lord and savior Jeb Bush winning France'
		    + '\n' +
		    'Jeb Wins Catalan Independence: Displays our lord and savior Jeb Bush winning Catalonia'
		    + '\n' +
		    'Jeb Wins The Universe: Displays our lord and savior Jeb Bush winning the universe'
		    + '\n' +
		    'Jeb Wins The World: Displays our lord and savior Jeb Bush winning the world'
		    + '\n' +
		    'Jeb Wins Canada: Displays our lord and savior Jeb Bush winning Canada'
		    + '\n' +
		    'Jeb Wins Russia: Displays our lord and savior Jeb Bush winning Russia'
		    + '\n' +
		    'Jeb Wins The Netherlands: Displays our lord and savior Jeb Bush winning the Netherlands'
		    + '\n' +
		    'Jeb Wins Congress: Displays our lord and savior Jeb Bush winning congress'
		    + '\n' +
		    'Jeb Wins Italy: Displays our lord and savior Jeb Bush winning Italy'
		    + '\n' +
		    'Jeb Wins Boot: Displays our lord and savior Jeb Bush winning the boot'
		    + '\n' +
		    'Jeb Wins New Zealand: Displays our lord and savior Jeb Bush winning New Zealand'
		    + '\n' + 'Uh Oh: Stinky' + '\n' + 'Skamtebord: Ha ha skamtebord'+'\n'+'Jeb Wins Everything: Jeb wins all the things'+'\n'+'We Should Really Ban That Ryan Kid: Gives you free candy')

  

	if 'jeb wins' == message.content.lower():
		await message.channel.send(file=discord.File('./Images/jebWins.jpg'))

	elif 'jeb wins france' == message.content.lower():
		await message.channel.send(file=discord.File('./Images/jebWinsFrance.jpg'))

	elif 'jeb wins catalan independence' == message.content.lower():
		await message.channel.send(
		    file=discord.File('./Images/Jeb Wins Catalan Edition.jpeg'))

	elif 'jeb wins the universe' == message.content.lower():
		await message.channel.send(file=discord.File('./Images/jebWinsUniverse.jpeg'))

	elif 'jeb wins the world' == message.content.lower():
		await message.channel.send(file=discord.File('./Images/jebWinsWorld.jpg'))

	elif 'jeb wins canada' == message.content.lower():
		await message.channel.send(file=discord.File('./Images/jebWinsCanada.png'))

	elif 'jeb wins russia' == message.content.lower():
		await message.channel.send(file=discord.File('./Images/jebWinsRussia.png'))

	elif 'jeb wins the netherlands' == message.content.lower():
		await message.channel.send(
		    file=discord.File('./Images/jebWinsTheNetherlands.png'))

	elif 'jeb wins congress' == message.content.lower():
		await message.channel.send(file=discord.File('./Images/jebWinsCongress.png'))

	elif 'jeb wins italy' == message.content.lower(
	) or 'jeb wins boot' == message.content.lower():
		await message.channel.send(file=discord.File('./Images/jebWinsBoot.jpg'))

	elif 'jeb wins new zealand' == message.content.lower():
		await message.channel.send(file=discord.File('./Images/jebWinsNewZealand.jpg'))

	elif 'jeb wins everything' == message.content.lower():
		await message.channel.send(file=discord.File('./Images/jebWins.jpg'))
		await message.channel.send(file=discord.File('./Images/jebWinsFrance.jpg'))
		await message.channel.send(
		    file=discord.File('./Images/Jeb Wins Catalan Edition.jpeg'))
		await message.channel.send(file=discord.File('./Images/jebWinsUniverse.jpeg'))
		await message.channel.send(file=discord.File('./Images/jebWinsWorld.jpg'))
		await message.channel.send(file=discord.File('./Images/jebWinsCanada.png'))
		await message.channel.send(file=discord.File('./Images/jebWinsRussia.png'))
		await message.channel.send(
		    file=discord.File('./Images/jebWinsTheNetherlands.png'))
		await message.channel.send(file=discord.File('./Images/jebWinsCongress.png'))
		await message.channel.send(file=discord.File('./Images/jebWinsBoot.jpg'))
		await message.channel.send(file=discord.File('./Images/jebWinsBoot.jpg'))
		await message.channel.send(file=discord.File('./Images/jebWinsNewZealand.jpg'))


	elif 'uh oh' == message.content.lower():
		await message.channel.send(
		    "*Fart*. Uh oh. Stinky. Poop. Ahahahahahaha. Poopies. Funny poopies. Elelelele. Haha. Funny poop, poop funny. Wheee. Haha. Yay for poopie. Good poopie. Poopie funny. Hahahahahahaha. Poop poop poop poop poop poop poop, funny. Yay. Fun fun poop! Tee, hee, hee. Poop poopie, yay. Poop make me happy, happy, happy. Yahahahahaha. Uh oh. I think I made a poopie. Poop in pants, no diaper, that's funny! Hahahahahahahahaha. Oopsie, poopy underwear now. Hee heehee. We want poopies. We want poopies. Hahahahahahahah. Hahahahahahahahahaha. Hahahaha. Poohoohoo-ah *cough*. Poop"
		)

	elif 'skamtebord' == message.content.lower():
		await message.channel.send(file=discord.File('./Images/skamtebord.jpg'))

	elif 'cuck shed' == message.content.lower():
		await message.delete()
		await message.channel.send(file=discord.File('./Images/cuckShed.png'))

	elif 'shutdown' == message.content.lower():
		print(message.author.id)

		try:
      
			await client.close()


		except:
			print("EnvironmentError")

	elif 'jeb' in message.content.lower() and message.channel.id != 660244746865737733:
		pics = ['./Images/jebWins.jpg', './Images/jebWinsFrance.jpg', './Images/Jeb Wins Catalan Edition.jpeg', './Images/jebWinsUniverse.jpeg', './Images/jebWinsWorld.jpg', './Images/jebWinsCanada.png', './Images/jebWinsRussia.png', './Images/jebWinsTheNetherlands.png', './Images/jebWinsCongress.png', './Images/jebWinsBoot.jpg', './Images/jebWinsNewZealand.jpg']
		num = rand(0, 10)
		await message.channel.send(
		    file=discord.File(pics[num]))
		
	if sentence_list[0] == ('maybot_say') and user != 'Fissics C Bot':
		await message.delete()
		string = ''
		for i in sentence1_list:
		  if i.lower() != 'maybot_say':
		    string += i
		    string += ' '
		await message.channel.send(string)

	await client.process_commands(message)   

	if sentence_list[0] == 'uwu' and sentence_list[1] == 'dis':
		await message.delete()
		msg = message.content.lower()
		uwuMsg = msg.replace('r', 'w')
		uwuMsg = uwuMsg.replace('R', 'W')
		uwuMsg = uwuMsg.replace('l', 'w')
		uwuMsg = uwuMsg.replace('L', 'W')
		count = 0
		finalMsg = ''
		for i in uwuMsg:
			if count < 8:
				count += 1
			else:
				finalMsg += i
		embed = discord.Embed(
			colour=discord.Colour(0x363940),
			title=finalMsg
			#description='This is a test'
    )
		if nick != 'None':
			embed.set_author(name=nick, icon_url=message.author.avatar_url)
		else:
			embed.set_author(name=user, icon_url=message.author.avatar_url)
		

		await message.channel.send(embed=embed)

	elif channel[0:3].lower() == 'uwu' and ('r' in message.content.lower() or 'l' in message.content.lower()):
		await message.delete()
		msg = message.content
		uwuMsg = msg.replace('r', 'w')
		uwuMsg = uwuMsg.replace('R', 'W')
		uwuMsg = uwuMsg.replace('l', 'w')
		uwuMsg = uwuMsg.replace('L', 'W')
		embed = discord.Embed(
			colour=discord.Colour(0x363940),
			title=uwuMsg
			#description='This is a test'
    )
		if nick != 'None':
			embed.set_author(name=nick, icon_url=message.author.avatar_url)
		else:
			embed.set_author(name=user, icon_url=message.author.avatar_url)
		

		await message.channel.send(embed=embed)

	newMessage = message.content.lower()
	newMessage_list = newMessage.split()
	if 'fuck' in message.content.lower() and ChristianServer:
		newMessage = newMessage.replace('fuck', 'frick')
		nono = True

	if ('damn' in message.content.lower() or 'damm' in message.content.lower()) and ChristianServer:
		newMessage = newMessage.replace('damn', 'darn')
		newMessage = newMessage.replace('damm', 'darn')
		nono = True

	if ('shit' in message.content.lower() and 'shitty' not in message.content.lower() and 'dipshit' not in message.content.lower() and 'bullshit' not in message.content.lower()) and ChristianServer:
		newMessage = newMessage.replace('shit', 'shoot')
		nono = True

	if 'shitty' in newMessage and ChristianServer:
		newMessage = newMessage.replace('shitty', 'stinky')
		nono = True

	if 'hell' in newMessage and ChristianServer:
		newMessage = newMessage.replace('hell', 'heck')
		nono = True

	if 'jesus' in newMessage and ChristianServer:
		newMessage = newMessage.replace('jesus', 'jeebus')
		nono = True

	if 'bitch' in newMessage and ChristianServer:
		newMessage = newMessage.replace('bitch', 'bruh')
		nono = True

	if 'god' in newMessage and ChristianServer:
		newMessage = newMessage.replace('god', 'gosh')
		nono = True

	if 'dick' in newMessage and ChristianServer:
		newMessage = newMessage.replace('dick', 'Richard')
		nono = True


	if 'retard' in newMessage and ChristianServer:
		newMessage = newMessage.replace('retarded', 'person with lower mental capacity, which is completely fine')
		newMessage = newMessage.replace('retard', 'person with lower mental capacity, which is completely fine')
		nono = True

	if 'dipshit' in newMessage and ChristianServer:
		newMessage = newMessage.replace('dipshit', 'dingus')
		nono = True

	if 'rarted' in newMessage and ChristianServer:
		newMessage = newMessage.replace('rarted', '||rarted||')
		nono = True

	if 'bullshit' in newMessage and ChristianServer:
		newMessage = newMessage.replace('bullshit', 'bullstinky')
		nono = True

	if ('ass' in newMessage or 'arse' in newMessage) and ChristianServer:
		newMessage = newMessage.replace('ass', 'bum')
		newMessage = newMessage.replace('arse', 'bum')
		nono = True

	if 'penis' in newMessage and ChristianServer:
		newMessage = newMessage.replace('penis', 'male genetalia')
		nono = True

	if 'boob' in newMessage and ChristianServer:
		newMessage = newMessage.replace('boob', 'breast')
		nono = True

	if 'cunt' in newMessage and ChristianServer:
		newMessage = newMessage.replace('cunt', 'cunnot')
		nono = True

	if 'slut' in newMessage and ChristianServer:
		newMessage = newMessage.replace('slut', 'sloot')
		nono = True

	if 'cuck shed' in newMessage and ChristianServer and newMessage != 'cuck shed':
		newMessage = newMessage.replace('cuck shed', '<:cuckshed:662509449264627733>')
		nono = True
		await message.channel.send(file=discord.File('./Images/cuckShed.png'))

		#await message.channel.send(nick + ': ' + newMessage)
	if nono:
		await message.delete()
		embed = discord.Embed(
			colour=discord.Colour(0x363940),
			title=newMessage
			#description='This is a test'
    )
		if nick != 'None':
			embed.set_author(name=nick, icon_url=message.author.avatar_url)
		else:
			embed.set_author(name=user, icon_url=message.author.avatar_url)
		

		await message.channel.send(embed=embed)

	if 'good bot' == message.content.lower():
		good_neg = False
		bad_neg = False
		file = open("goodBadBot.txt","r") 
		contents = file.readlines()
		file.close()
		print(contents) # ['good = 0\n', 'bad = 0']
		good = contents[0]
		good_num = ''
		for i in good:
			try:
				x = int(i)
				good_num += str(i)
			except:
				if i == '-':
					good_neg = True
				pass
		if good_neg:
			good_sign = -1
		else:
			good_sign = 1
		good_int = good_sign * int(good_num)
		bad = contents[1]
		bad_num = ''
		for i in bad:
			try:
				x = int(i)
				bad_num += str(i)
			except:
				if i == '-':
					bad_neg = True
				pass
		if bad_neg:
			bad_sign = -1
		else:
			bad_sign = 1
		bad_int = bad_sign * int(bad_num)
		score = 10 * (1 + good_int - bad_int)
		print(score)
		newList = ['good = ' + str(int(good_sign * good_num) + 1) + '\n', contents[1], 'score = ' + str(score)]
		file = open("goodBadBot.txt","w")
		file.writelines(newList)
		file.close()
		await message.channel.send("Maybot's rating: " + str(score))

	if 'bad bot' == message.content.lower():
		good_neg = False
		bad_neg = False
		file = open("goodBadBot.txt","r") 
		contents = file.readlines()
		file.close()
		print(contents) # ['good = 0\n', 'bad = 0']
		good = contents[0]
		good_num = ''
		for i in good:
			try:
				x = int(i)
				good_num += str(i)
			except:
				if i == '-':
					good_neg = True
				pass
		if good_neg:
			good_sign = -1
		else:
			good_sign = 1
		good_int = good_sign * int(good_num)
		bad = contents[1]
		bad_num = ''
		for i in bad:
			try:
				x = int(i)
				bad_num += str(i)
			except:
				if i == '-':
					bad_neg = True
				pass
		if bad_neg:
			bad_sign = -1
		else:
			bad_sign = 1
		bad_int = bad_sign * int(bad_num)
		score = 10 * (-1 + good_int - bad_int)
		print(score)
		newList = [contents[0], 'bad = ' + str(int(bad_sign * bad_num) + 1) + '\n', 'score = ' + str(score)]
		file = open("goodBadBot.txt","w")
		file.writelines(newList)
		file.close()
		await message.channel.send("Maybot's rating: " + str(score))
	
	if '69' in message.content.lower():
		await message.channel.send('Nice.')

	if 'good evening' in message.content.lower() and user != 'Fissics C Bot':
		await message.channel.send('Good evening ' + nick)
'''
	file = open('Message Date.txt', 'r')
	contents = file.readlines()
	file.close()
	found = False
	for i in contents:
		if user in i:
			pos = contents.index(i)
			i.replace(user, '')
			if i != str(date.today()):
				await message.channel.send(user + ' has earned a gold coin')
				contents.pop(pos)
				file = open('Message Date.txt', 'w').close()

				file = open('Message Date.txt', 'a')
				for i in contents:
					file.write(i)
					file.write('\n')
				file.close()
				file = open('Message Date.txt', 'a')
				file.write(user + str(date.today()))
				file.write('\n')
				file.close()
			found = True
	if not found:
		await message.channel.send(user + ' has earned a gold coin')
		file = open('Message Date.txt', 'w').close()
		file = open('Message Date.txt', 'a')
		for i in contents:
			file.write(i)
			file.write('\n')
		file.close()
		file = open('Message Date.txt', 'a')
		file.write(user + str(date.today()))
		file.write('\n')
		file.close()
'''		

@client.command()
async def isTylerDum(ctx):
	await ctx.send('TylerIsDum = True')

@client.command(pass_context=True)
async def play(ctx, url):
  guild = ctx.message.guild
  voice_client = guild.voice_client
  player = await voice_client.create_ytdl_player(url)
  players[server.id] = player
  player.start()

@client.command()
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command()
async def ping(ctx, num):
	List = ctx.message.content.split()
	print(List[1])
	if int(List[2]) > 50 and List[1] != '<@!427775962441056258>':
		await ctx.channel.send('Too large')
	else:
		try:
			for count in range(int(List[2])):
				await ctx.channel.send(List[1])
		except:
			await ctx.channel.send('Error')

@client.command(aliases=['Suggest'])
async def suggest(ctx):
	file = open('suggestions.txt', 'a')
	suggestion_list = ctx.message.content.split()
	suggestion = ''
	for i in suggestion_list:
		if i.lower() != '.suggest':
			suggestion += i + ' '
	file.write(suggestion + '\n')
	file.close()
	await ctx.channel.send('Thank you for the suggestion')

@client.command()
async def inventory(ctx):
	await ctx.message.delete()
	file = open('Inventories.txt', 'r')
	contents = file.readlines()
	file.close()
	try:
		pos = contents.index(str(ctx.message.author.name) + '#' + str(ctx.message.author.discriminator) + '\n')
	except:
		file = open('Inventories.txt', 'a')
		file.write('\n')
		file.write(str(ctx.message.author.name) + '#' + str(ctx.message.author.discriminator) + '\n')
		file.write('\n')
		file.close()
		pos = contents.index(str(ctx.message.author.name) + '#' + str(ctx.message.author.discriminator) + '\n')
	print(pos)

	inv = []
	while contents[pos] != '\n':
		term = contents[pos].replace('\n', '')
		inv.append(term)
		pos += 1
	inv.pop(0)
	print(inv)
	num_coin = 0
	num_bcram = 0
	num_vcram = 0
	num_rcram = 0
	num_andys_trust = 0
	for i in inv:
		if i == 'GOLD COIN':
			num_coin += 1
		if i == 'BERRY CRAM':
			num_bcram += 1
		if i == 'VERY BERRY CRAM':
			num_vcram += 1
		if i == 'RASPBERRY CRAM':
			num_rcram += 1
		if i == 'ANDYS TRUST':
			num_andys_trust += 1
	print(num_coin)
	if ctx.message.author.display_name != 'None':
		nickname = True
		nick = str(ctx.message.author.display_name)
	else:
		nickname = False
		nick = str(ctx.message.author.name)
		
	embed = discord.Embed(
		colour=discord.Colour(0x363940),
		title=nick + "'s inventory"
		#description='This is a test'
   )
#	if nick != 'None':
#		embed.set_author(name=nick, icon_url=message.author.avatar_url)
#	else:
#		embed.set_author(name=user, icon_url=message.author.avatar_url)
	embed.add_field(name='Gold Coins', value=num_coin, inline=False)
	embed.add_field(name='Berry Cram', value=num_bcram, inline=True)
	embed.add_field(name='Very Berry Cram', value=num_vcram, inline=True)
	embed.add_field(name='Raspberry Cram', value=num_rcram, inline=True)
	if num_andys_trust != 0:
		embed.add_field(name="Andy's Trust", value=num_andys_trust, inline=True)

	await ctx.message.channel.send(embed=embed)


@client.command()
async def goodbye(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)

keep_alive()
TOKEN = os.environ.get('DISCORD_BOT_SECRET')
client.run(TOKEN)
