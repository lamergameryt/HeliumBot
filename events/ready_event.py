import discord
from discord.ext import commands


class ReadyEvent(commands.Cog):
    """
    This class is used to setup the bot when it is initialized.
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'The bot is online with the name {self.bot.user.name}.')
        await self.bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name='>help | I love you <3'))


def setup(bot: commands.Bot):
    bot.add_cog(ReadyEvent(bot))
