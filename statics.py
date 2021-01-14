import discord
from datetime import datetime


def get_embed(description: str, title: str = None):
    embed = discord.Embed(description=description, color=0xeb4034, timestamp=datetime.now())
    if title is not None:
        embed.title = title
    embed.set_footer(text='Made by LamerGamerYT#7552')

    return embed
