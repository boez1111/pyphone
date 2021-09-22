import requests
from discord.ext import commands
import discord
from datetime import datetime

bot = commands.Bot(command_prefix="--", help_command=None)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='--help >
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
        embed = discord.Embed(title="The command looks like this: ```--scan [number with country code]>
                              colour=000000, timestamp=ctx.message.created_at)
        await ctx.send(embed=embed)
    phone_number = str(number)
    print(number)
    print("---------------")

    access_key = 'fgh2v3gjjz1g' #key from numverify.com
    url = 'http://apilayer.net/api/validate?access_key=' + access_key + '&number=' + phone_number
    response = requests.get(url)
    answer = response.json()
    print(answer)
    if answer["valid"] == True:

        embed2 = discord.Embed(title=f"**Informationen über die Telefonnummer {phone_number}**!",descript>
        embed2.add_field(name="Gültigkeit", value=answer['valid'], inline=False)
        embed2.add_field(name="Nummer", value=answer['number'], inline=False)
        embed2.add_field(name="Lokales Format", value=answer['local_format'], inline=False)
        embed2.add_field(name="Internationales Format", value=answer['international_format'], inline=Fals>
        embed2.add_field(name="Landespräfix", value=answer['country_prefix'], inline=False)
        embed2.add_field(name="Landescode", value=answer['country_code'], inline=False)
        embed2.add_field(name="Land`", value=answer['country_name'], inline=False)
        embed2.add_field(name="Anbieter", value=answer['carrier'], inline=False)
        embed2.add_field(name="Nummerntyp", value=answer['line_type'], inline=False)
        embed2.timestamp = datetime.utcnow()
        await ctx.send(embed=embed2)
    else:
        ctx.send("not a valid number")


bot.run("token") #your bot token
