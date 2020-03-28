import discord, random
from discord.ext import commands
from discord.ext.commands import Bot

TOKEN = 'NjkxNjczMTAyNDUwNjg4MDkx.XnkGWA._m4PK5bMP5n8TguYozFIgzVANBs'

BOT_PREFIX = ("$")
bot = commands.Bot(command_prefix=BOT_PREFIX)

@bot.event
async def on_ready():
	print ("------------------------------------")
	print ("Bot Name: " + bot.user.name)
	print ("Bot ID: " + str(bot.user.id))
	print ("Discord Version: " + discord.__version__)
	print ("------------------------------------")

@bot.command(pass_context=True)
async def info(ctx):
	embed = discord.Embed(title="PwrBot", description="Unofficial PwrBot")
	await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def pomoc(ctx):
	embed = discord.Embed(title="Tomasz Kolęda")
	embed.add_field(name="$info", value="Informacje na temat bot'a", inline=False)
	embed.add_field(name="$szkaluj **User**", value="Szkaluje użytkownika", inline=False)
	embed.add_field(name="$toxic **User**", value="Upomina o byciu toksycznym", inline=False)
	embed.add_field(name="$code_blocks", value="Mem z C::B = HIV", inline=False)
	embed.add_field(name="$urodziny **User**", value="Wstawia zdjecie tortu", inline=False)
	embed.add_field(name="$pomoc", value="Wypisuje podstawowe komendy", inline=False)
	await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def ping(ctx, member : discord.Member):
	await ctx.send(member.mention)

@bot.command(pass_context=True)
async def szkaluj(ctx, member : discord.Member):
	zwrotySzkalujace = 	['{0} ma małego',
					 	'{0} ogaląda Zelenta',
					 	'{0} zapomniał o N',
					 	'{0} śpi z mamą',
					 	'{0} przejechał kota sąsiada']
	wyszkalowane = random.choice(zwrotySzkalujace)
	await ctx.send(wyszkalowane.format(member.mention))

@bot.command(pass_context=True)
async def toxic(ctx, member : discord.Member):
	await ctx.send("{0} ale ty jesteś toksyczny".format(member.mention))

@bot.command(pass_context=True)
async def code_blocks(ctx):
	await ctx.send(file=discord.File('cbhiv.png'))

@bot.command(pass_context=True)
async def urodziny(ctx, member : discord.Member):
	await ctx.send(file=discord.File('uro.jpg'))

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
		await ctx.message.guild.kick(user,reason = "XD")

bot.run(TOKEN)