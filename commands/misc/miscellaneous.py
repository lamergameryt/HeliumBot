from discord.ext import commands
import statics
import time
import requests

QUOTE_API = 'https://zenquotes.io/api/random'


class Miscellaneous(commands.Cog, name='misc'):
    """
    A set of miscellaneous commands for various purposes.
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(
        brief="Check the bot's ping to your server.",
        help="Measures the duration between when a message is sent and it is received by discord."
    )
    async def ping(self, ctx: commands.Context):
        before = time.monotonic()
        message = await ctx.send(embed=statics.get_embed('Pong!'))
        delta: int = round((time.monotonic() - before) * 1000)
        await message.edit(embed=statics.get_embed(f'Pong! `{delta} ms`'))

    @commands.command(
        brief='I need, motivation.',
        help='Get a motivating quote to inspire your ass off.'
    )
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def quote(self, ctx: commands.Context):
        response = requests.get(QUOTE_API).json()
        await ctx.send(embed=statics.get_embed(response[0]['q'], 'Here is a random quote for you'))


def setup(bot: commands.Bot):
    bot.add_cog(Miscellaneous(bot))
