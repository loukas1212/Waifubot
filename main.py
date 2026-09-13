#!/usr/bin/python3
import asyncio
import discord
from discord.ext import commands
from colorama import Fore, Style, init
import os
from dotenv import load_dotenv
from modules.fnc_embed import simple_embed

init()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
COGS_PATH = os.path.join(BASE_DIR, "cogs")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="-", intents=intents) # choix du prefix

load_dotenv()

##############################################
# Verif des rôles Admins, et de loukas

# Synchronisation des cogs
async def load_cogs():
    loaded = 0
    failed = 0

    for root, dirs, files in os.walk(COGS_PATH):
        for filename in files:
            if filename.endswith(".py") and not filename.startswith("_"):

                # Build cogs path
                relative_path = os.path.relpath(os.path.join(root, filename), BASE_DIR)
                module_path = relative_path[:-3].replace(os.sep, ".")

                try:
                    await bot.load_extension(module_path)
                    print(Fore.CYAN + f"Cog chargé : {module_path}" + Style.RESET_ALL)
                    loaded += 1
                except Exception as err:
                    print(Fore.RED + f"Erreur survenu lors du chargement de {module_path} : {err}" + Style.RESET_ALL)
                    failed += 1

    print(Fore.GREEN + f"{loaded} cogs chargés" + Style.RESET_ALL)
    print(Fore.RED + f"{failed} cogs en erreur" + Style.RESET_ALL)

# Événement : le bot est prêt
@bot.event
async def on_ready():

    print(Fore.GREEN + f"{bot.user}" + Style.RESET_ALL + " est connecté et prêt !")




##########################################################################################################################################

# Commande de version (-version)
@bot.command()
async def version(ctx):
    embed = simple_embed(
        "Version",
        "Version du 09/2026\n"
        "ID : v2.0\n"
        "Type : Completed Version",
        color="vert"
    )
    await ctx.send(embed=embed)

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




async def main():
    async with bot:
        await load_cogs()
        await bot.start(os.getenv("BOT_TOKEN"))


asyncio.run(main())