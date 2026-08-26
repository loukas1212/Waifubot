#!/usr/bin/python3
import discord
from discord.ext import commands
from colorama import Fore, Style, init
import os
from dotenv import load_dotenv
from modules import apicall
from modules.fnc_embed import simple_embed


intents = discord.Intents.default()
bot = commands.Bot(command_prefix="-", intents=intents) # choix du prefix
intents.message_content = True

load_dotenv() 

##############################################
# Verif des rôles Admins, et de loukas
# Événement : le bot est prêt
@bot.event
async def on_ready():

    print(Fore.GREEN + f"{bot.user}" + Style.RESET_ALL + " est connecté et prêt !")




##########################################################################################################################################

# Commande de version (/version)
@bot.command()
async def version(ctx):
    embed = simple_embed(
        "Version",
        "Version du 08/2026\n"
        "ID : v1.0 revision 1\n"
        "Type : Uncompleted Version",
        color="vert"
    )
    await ctx.send(embed=embed)

##############################################
# API SFW 

@bot.command()
async def waifu(ctx):
    id, image = apicall.waifuapi()
    await ctx.send(f"{image}\nID = {id}")

@bot.command()
async def waifu_maid(ctx):
    id, image = apicall.waifuapi_sfw_tag("maid")
    await ctx.send(f"{image}\nID = {id}")


@bot.command()
async def waifu_waifu(ctx):
    id, image = apicall.waifuapi_sfw_tag("waifu")
    await ctx.send(f"{image}\nID = {id}")


@bot.command()
async def waifu_marino(ctx):
    id, image = apicall.waifuapi_sfw_tag("marin-kitagawa")
    await ctx.send(f"{image}\nID = {id}")


@bot.command()
async def waifu_mori_calliope(ctx):
    id, image = apicall.waifuapi_sfw_tag("mori-calliope")
    await ctx.send(f"{image}\nID = {id}")


@bot.command()
async def waifu_raiden_shogun(ctx):
    id, image = apicall.waifuapi_sfw_tag("raiden-shogun")
    await ctx.send(f"{image}\nID = {id}")


@bot.command()
async def waifu_selfies(ctx):
    id, image = apicall.waifuapi_sfw_tag("selfies")
    await ctx.send(f"{image}\nID = {id}")


@bot.command()
async def waifu_uniform(ctx):
    id, image = apicall.waifuapi_sfw_tag("uniform")
    await ctx.send(f"{image}\nID = {id}")


@bot.command()
async def waifu_genshin(ctx):
    id, image = apicall.waifuapi_sfw_tag("genshin-impact")
    await ctx.send(f"{image}\nID = {id}")


# API NSFW

# HENTAI
@bot.command()
async def waifu_hentai(ctx):
    if not ctx.channel.is_nsfw():
        await ctx.send("Commande utilisable uniquement dans un salon NSFW.")
        return

    id, image = apicall.waifuapi_nsfw("hentai")
    await ctx.send(f"{image}\nID = {id}")


# ERO
@bot.command()
async def waifu_ero(ctx):
    if not ctx.channel.is_nsfw():
        await ctx.send("Commande utilisable uniquement dans un salon NSFW.")
        return

    id, image = apicall.waifuapi_nsfw("ero")
    await ctx.send(f"{image}\nID = {id}")


# ASS
@bot.command()
async def waifu_ass(ctx):
    if not ctx.channel.is_nsfw():
        await ctx.send("Commande utilisable uniquement dans un salon NSFW.")
        return

    id, image = apicall.waifuapi_nsfw("ass")
    await ctx.send(f"{image}\nID = {id}")


# MILF
@bot.command()
async def waifu_milf(ctx):
    if not ctx.channel.is_nsfw():
        await ctx.send("Commande utilisable uniquement dans un salon NSFW.")
        return

    id, image = apicall.waifuapi_nsfw("milf")
    await ctx.send(f"{image}\nID = {id}")


# ORAL
@bot.command()
async def waifu_oral(ctx):
    if not ctx.channel.is_nsfw():
        await ctx.send("Commande utilisable uniquement dans un salon NSFW.")
        return

    id, image = apicall.waifuapi_nsfw("oral")
    await ctx.send(f"{image}\nID = {id}")

# PAIZURI
@bot.command()
async def waifu_paizuri(ctx):
    if not ctx.channel.is_nsfw():
        await ctx.send("Commande utilisable uniquement dans un salon NSFW.")
        return

    id, image = apicall.waifuapi_nsfw("paizuri")
    await ctx.send(f"{image}\nID = {id}")

# ECCHI
@bot.command()
async def waifu_ecchi(ctx):
    if not ctx.channel.is_nsfw():
        await ctx.send("Commande utilisable uniquement dans un salon NSFW.")
        return

    id, image = apicall.waifuapi_nsfw("ecchi")
    await ctx.send(f"{image}\nID = {id}")

##############################################
# Commande de help, utilisation : -commandes
@bot.command()
async def commandes(ctx):
    await ctx.send(embed=simple_embed(
        "Liste des commandes Waifu",
        f"**Commandes SFW**\n"
        f"-waifu\n"
        f"-waifu_maid\n"
        f"-waifu_waifu\n"
        f"-waifu_marino\n"
        f"-waifu_mori_calliope\n"
        f"-waifu_raiden_shogun\n"
        f"-waifu_selfies\n"
        f"-waifu_uniform\n"
        f"-waifu_genshin\n"
        f"--------------------------------------------------\n"
        f"**Commandes NSFW**\n"
        f"-waifu_hentai\n"
        f"-waifu_ero\n"
        f"-waifu_ass\n"
        f"-waifu_milf\n"
        f"-waifu_oral\n"
        f"-waifu_paizuri\n"
        f"-waifu_ecchi\n"
        f"--------------------------------------------------\n",
        color="bleu"
    ))




bot.run(os.getenv("BOT_TOKEN"))