import discord
import datetime
import random
from discord.ext import commands

TOKEN = 'INSERT_TOKEN'

description = '''Pythontestbot'''
bot = commands.Bot(command_prefix='!', description=description) 
#Autostart
@bot.event
async def on_ready():
    print('Eingeloggt als:')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
#BETA (muss noch ausgebessert werden)
@bot.command()
async def d(a:int, b:int):
	"""d <Anzahl der Würfe> <höchste Zahl>"""
	zahl=0
	for i in range(a):
		zahl+=random.randint(1, b)
	await bot.say(zahl)
#Testkommandos
@bot.command()
async def hellothere():
    """Meme"""
    await bot.say("General Kenobi")

@bot.command()
async def miau():
	"""Katzenfotos!"""
	await bot.say("https://media3.giphy.com/media/nNxT5qXR02FOM/giphy.gif")
#Mathe
@bot.command()
async def add(left : int, right : int):
	"""Addition"""
	await bot.say(left + right)

@bot.command()
async def sub(left : int, right : int):
	"""Subtraktion"""
	await bot.say(left - right)

@bot.command()
async def mult(left : int, right : int):
	"""Multiplikation"""
	await bot.say(left * right)

@bot.command()
async def div(left : int, right : int):
	"""Division"""
	await bot.say(left / right)

@bot.command()
async def mod(left : int, right : int):
	"""Modulo"""
	await bot.say(left % right)
#Sonstiges
@bot.command(pass_context=True)
async def münzwurf(ctx):
	variable = [
		"Kopf",
		"Zahl"]
	await bot.say(random.choice(variable))
#MAIQ
@bot.command(pass_context=True)
async def quote(ctx):
	"""Wertvolle Zitate des M'aiq"""
	variable = [
        	"Drachen waren nie weg, sie waren einfach unsichtbar und sehr, sehr ruhig.",
        	"Einige sagen, Alduin ist Akatosh, manche sagen, M'aiq ist ein Lügner. Ich würde keines von beidem glauben.",
		"Es spielt für M'aiq keine Rolle, wie stark oder schlau jemand ist. Es kommt nur darauf an, was man tun kann.",
		"Etwas Seltsames passiert mit den Khajiit, wenn sie in Himmelsrand ankommen.",
		"M'aiq erinnert sich nicht an seine Kindheit. Vielleicht hatte er nie eine.",
		"M'aiq ging einst nach Hoch-Hrothgar. So viele Schritte, er konnte sie gar nicht zählen.",
		"M'aiq hat gehört, dass die Menschen in Himmelsrand schöner sind als in Cyrodiil. Aber für M'aiq sind alle Menschen gleich.",
		"M'aiq hat genug geredet.",
		"M'aiq hört viele Geschichte vom Krieg ... doch nur wenige sind wahr.",
		"M'aiq ist immer auf der Suche nach Greifzirkeln, doch er findet sie nicht. Wo könnten sie sein?",
		"M'aiq ist jetzt müde. Geht jemand anderem auf die Nerven.",
		"M'aiq ist sehr praktisch veranlagt. Er braucht keine Mystik.",
		"M'aiq kann auf dem Land schnell reisen, manche sind faul und nehmen einen Wagen. Es ist alles gleich für M'aiq.",
		"M'aiq liebt die Leute von Himmelsrand. Sie sagen viele interessante Sachen zueinander.",
		"M'aiq sah eine Schlammkrabbe. Schreckliche Kreaturen.",
		"M'aiq trägt zwei Waffen, um sicher zu gehen. Was, wenn eine kaputt geht? Das wäre sehr ungünstig.",
		"M'aiq wünscht Euch alles Gute.",
		"M'aiq weiß viel und erzählt nicht alles. M'aiq weiß viele Dinge, die andere nicht wissen.",
		"M'aiqs Vater hieß M'aiq. Genauso wie der Vater von M'aiqs Vater. Das behauptet zumindest sein Vater.",
		"M'aiq versteht nicht, was an den Schreien so beeindruckend ist. M'aiq kann schreien wann immer er will.",
		"Nord nehmen ihre Bärte sehr ernst. So viel Bärte. M'aiq glaubt, sie sind neidisch auf die Mähnen von Khajiit.",
		"Schnee fällt. Warum sich Sorgen machen, wohin es geht? M'aiq denkt, die Schneeflocken sind hübsch.",
		"Sobald M'aiq in Rifton in Schwierigkeiten gerät, flieht er nach Windhelm. Es ist gut, dass es dort niemanden interessiert.",
		"Viel Schnee in Himmelsrand. Genug Schnee. M'aiq will nicht, dass es mehr wird.",
		"Warum üben Soldaten eigentlich mit Zielscheiben? Man lernt viel besser, wenn man echte Personen trifft.",
		"Was bedeutet es, Magie zu kombinieren? Magie plus Magie ist immer noch Magie.",
		"Wenn Ihr zwei Waffen habt, lasst das Blocken lieber sein. Das verwirrt Euch bloß. Es ist sowieso viel besser, gleich zweimal zuzuschlagen.",
		"Werbären? Wer? Bären? Männer, die Bären sind?",
		"Woher weiß man, ob es die Stadt Winterfeste überhaupt gibt? M'aiq hat sie nicht mit seinen eigenen Augen gesehen. Ihr etwa?",
		"Zu viel Magie kann gefährlich sein. M'aiq hatte einmal zwei Zauber und verbrannte sich seine Milchsemmel."
	]
	await bot.say(random.choice(variable))
#ENDE
bot.run(TOKEN)
