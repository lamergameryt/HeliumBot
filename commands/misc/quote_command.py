from discord.ext import commands
import statics
import requests

QUOTE_API = 'https://zenquotes.io/api/random'


class QuoteCommand(commands.Cog):
    """
    Get a nice little quote to inspire you ;)
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def quote(self, ctx):
        response = requests.get(QUOTE_API).json()
        await ctx.send(embed=statics.get_embed(response[0]['q'], 'Here is a random quote for you'))


def setup(bot: commands.Bot):
    bot.add_cog(QuoteCommand(bot))
