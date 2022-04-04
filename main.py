import discord,re,json,random,asyncio
from discord.ext import commands,tasks
from discord.ext.commands import MissingPermissions
from time import time
from keep_alive import keep_alive

perms = discord.Intents(
    messages=True,
    guilds=True,
    reactions=True, 
    members=True, 
    presences=True,
    dm_messages = False,
    dm_reactions = False) 

with open('config.json') as f:
    config = json.load(f)
    token = config["token"]
    prefix = config["prefix"]
    startup = config["message1"]

activity=discord.Activity(type=discord.ActivityType.listening, name=f"No bitches by FPYF")

bot = commands.Bot(
  command_prefix=prefix,
  case_insensitive = True,
  intents = perms, 
  activity = activity)

@bot.event
async def on_ready():
  print(startup)

@bot.event
async def on_member_join(member):
  channel = bot.get_channel(957488765457301596)
  channell = bot.get_channel(958566624624001044)
  embed = discord.Embed(title = "Account joined",description = f"The user {member.name} has attempted joining us.")
  embed.set_author(name=str(member.name), icon_url=member.avatar_url)
  
  await channell.send(f"`|Mention: `{member.mention}` |Name: {member} |ID: {member.id}`")
  await channel.send(embed = embed)
  await member.ban(reason = "Attempted join")
  if member.id == 649755456927170601:
    await channel.send(f"^^^^^^LMFAO A FYPF SHITTER TRIED JOINING!^^^^^^")
  if member.id == 622442733294059526:
    await channel.send(f"^^^^^^LMFAO A FYPF SHITTER TRIED JOINING!^^^^^^")
  if member.id == 758887378520768544:
    await channel.send(f"^^^^^^LMFAO A FYPF SHITTER TRIED JOINING!^^^^^^")
  if member.id == 836361597701193748:
    await channel.send(f"^^^^^^LMFAO A FYPF SHITTER TRIED JOINING!^^^^^^")
@bot.command()
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	
	member_name, member_discriminator = member.split('#')
	for ban_entry in banned_users:
		user = ban_entry.user
		
		if (user.name, user.discriminator) == (member_name, member_discriminator):
 			await ctx.guild.unban(user)
 			await ctx.channel.send(f"Unbanned: {user.mention}")

@bot.command()
async def boot(ctx, member : discord.Member = None):
  await member.kick(reason = "got the boot")
  await ctx.send(f"f's to {member} he got booted")

    
keep_alive()
bot.run(token)