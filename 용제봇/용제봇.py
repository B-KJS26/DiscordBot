#run.py
import discord

client = discord.Client(command_prefix="$")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) #봇이 실행되면 콘솔창에 표시

@client.event()
async def hello(ctx):
    await ctx.send("hello")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
    	await ctx.send("명령어를 찾지 못했습니다")
    	
client.run('Token자리')
