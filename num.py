import requests
from discord.ext import commands
import discord
from datetime import datetime

bot = commands.Bot(command_prefix="--", help_command=None)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='--help')
    print("Ready")
@bot.command()
async def help(ctx):
    embed = discord.Embed(
        color=discord.Color.blue()
    )
    embed.add_field(name="Commands", value="ping, scan", inline=False)
    embed.set_author(name="Help",icon_url=bot.user.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000, 2)
    await ctx.send(f"`{latency} ms`")


@bot.command()
async def scan(ctx, number=None):
    if number is None:
        embed = discord.Embed(title="The command looks like this: ```--scan [number with country code]```,
                              colour=000000, timestamp=ctx.message.created_at)
        await ctx.send(embed=embed)
    phone_number = str(number)
    print(number)
    print("Searching...")

    access_key = 'fgh2v3gjjz1g' #key from numverify.com
    url = 'http://apilayer.net/api/validate?access_key=' + access_key + '&number=' + phone_number
    response = requests.get(url)
    answer = response.json()
    print(answer)
    if answer["valid"] == True:

        embed2 = discord.Embed(title=f"**Information about the Number {phone_number}**",description="The information may not be 100% correct. Deviations possible.",
        embed2.add_field(name="Valid", value=answer['valid'], inline=False)
        embed2.add_field(name="Number", value=answer['number'], inline=False)
        embed2.add_field(name="Local Format", value=answer['local_format'], inline=False)
        embed2.add_field(name="International Format ", value=answer['international_format'], inline=Fals>
        embed2.add_field(name="Country Prefix", value=answer['country_prefix'], inline=False)
        embed2.add_field(name="Country Code", value=answer['country_code'], inline=False)
        embed2.add_field(name="Country Name", value=answer['country_name'], inline=False)
        embed2.add_field(name="Carrier", value=answer['carrier'], inline=False)
        embed2.add_field(name="Line Type", value=answer['line_type'], inline=False)
        embed2.timestamp = datetime.utcnow()
        await ctx.send(embed=embed2)
    else:
        ctx.send("not a valid number")


bot.run("token") #your bot token
