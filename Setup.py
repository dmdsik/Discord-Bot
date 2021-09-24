import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online, activity=None)

@bot.command()
async def 따라하기(ctx, *, number):
    await ctx.send(embed = discord.Embed(titlte = '따라하기', description = text, color = 0x00ff00))

bot.run('ODkwOTQwNjU0MDU2NzkyMDc0.YU3HJA.9UeBqmWFMq02HA9dfL9a05cAEsc')