#!/usr/bin/python3

import discord
from discord.ext import commands
from discord.ui import Button, View



### primary (bleu)
### secondary (gris)
### success (vert)
### danger (rouge)

def color2hex(color):
    if color == "rouge":
        color = 0xFF0000
    elif color == "bleu":
        color = 0x0D00FF
    elif color == "orange":
        color = 0xFF8000
    elif color == "jaune":
        color = 0xFFE600
    elif color == "vert":
        color = 0x40FF00
    elif color == "noir":
        color = 0x000000
    elif color == "blanc":
        color = 0xFFFFFF
    
    return color

def simple_embed(title, description, color):
    embed = discord.Embed(
        title=f"**{title}**",
        description=f"{description}",
        color=color2hex(color),
    )
    return embed    
