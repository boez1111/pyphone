import requests
from discord.ext import commands
import discord
from datetime import datetime

command_prefix = "--"      #choose any prefix you want
token = ""         #your bot token
admins = []  #id of users, who are allowed to use the scan command

bot = commands.Bot(command_prefix=command_prefix, help_command=None)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='--help'))
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
async def scanm(ctx, number=None):
    if number is None:
        embed = discord.Embed(title="Der Befehl sieht wie folgt aus: ```--scanm [number with country code]```",
                              colour=000000, timestamp=ctx.message.created_at)
        await ctx.send(embed=embed)
    phone_number = str(number)
    print(number)
    print("---------------")

    access_key = '239270931798b5f0312f66cd4411d58e'
    url = 'http://apilayer.net/api/validate?access_key=' + access_key + '&number=' + phone_number
    response = requests.get(url)
    answer = response.json()
    print(answer)

    embed1 = discord.Embed(
        title="Error!",
        color=discord.Color.red(),
        description=f"{ctx.author.mention} Du hast keine Berechtigung."

    )

    if ctx.author.id not in admins:
        await ctx.reply(embed=embed1, mention_author=False)
        await ctx.message.add_reaction("❌")

    else:
        try:
            if answer["valid"] == True:
                embed2 = discord.Embed(title=f"__**Informationen über die Telefonnummer {phone_number}**__",
                                       description="Diese Informationen sind nicht zu 100% genau! Abweichungen sind möglich.",
                                       colour=discord.Colour.green(), timestamp=ctx.message.created_at)
                embed2.add_field(name="Gültigkeit", value=answer['valid'], inline=False)
                embed2.add_field(name="Nummer", value=answer['number'], inline=False)
                embed2.add_field(name="Lokales Format", value=answer['local_format'], inline=False)
                embed2.add_field(name="Internationales Format", value=answer['international_format'], inline=False)
                embed2.add_field(name="Landespräfix", value=answer['country_prefix'], inline=False)
                embed2.add_field(name="Landescode", value=answer['country_code'], inline=False)
                embed2.add_field(name="Land", value=answer['country_name'], inline=False)
                embed2.add_field(name="Anbieter", value=answer['carrier'], inline=False)
                embed2.add_field(name="Nummerntyp", value=answer['line_type'], inline=False)
                embed2.timestamp = datetime.utcnow()
                await ctx.reply(embed=embed2, mention_author=False)
                await ctx.message.add_reaction('✅')

        except Exception as e:
            raise e

@bot.command()
async def scanl(ctx, number=None):
    if number is None:
        embed = discord.Embed(title="Der Befehl sieht wie folgt aus: ```--scanl [number with country code]```",
                              colour=000000, timestamp=ctx.message.created_at)
        await ctx.send(embed=embed)
    phone_number = str(number)
    print(number)
    print("---------------")

    access_key = '239270931798b5f0312f66cd4411d58e'
    url = 'http://apilayer.net/api/validate?access_key=' + access_key + '&number=' + phone_number
    response = requests.get(url)
    answer = response.json()
    print(answer)

    embed1 = discord.Embed(
        title="Error!",
        color=discord.Color.red(),
        description=f"{ctx.author.mention} Du hast keine Berechtigung."

    )

    if ctx.author.id not in admins:
        await ctx.reply(embed=embed1, mention_author=False)
        await ctx.message.add_reaction("❌")

    else:
        try:
            if answer["valid"] == True:
                embed2 = discord.Embed(title=f"__**Informationen über die Telefonnummer {phone_number}**__",
                                       description="Diese Informationen sind nicht zu 100% genau! Abweichungen sind möglich.",
                                       colour=discord.Colour.green(), timestamp=ctx.message.created_at)
                embed2.add_field(name="Gültigkeit", value=answer['valid'], inline=False)
                embed2.add_field(name="Nummer", value=answer['number'], inline=False)
                embed2.add_field(name="Lokales Format", value=answer['local_format'], inline=False)
                embed2.add_field(name="Internationales Format", value=answer['international_format'], inline=False)
                embed2.add_field(name="Landespräfix", value=answer['country_prefix'], inline=False)
                embed2.add_field(name="Landescode", value=answer['country_code'], inline=False)
                embed2.add_field(name="Land", value=answer['country_name'], inline=False)
                embed2.add_field(name="Standort", value=answer['location'], inline=False)
                embed2.add_field(name="Nummerntyp", value=answer['line_type'], inline=False)
                embed2.timestamp = datetime.utcnow()
                await ctx.reply(embed=embed2, mention_author=False)
                await ctx.message.add_reaction('✅')

        except Exception as e:
            raise e


bot.run(token)
