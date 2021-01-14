from discord.ext import commands
import statics
import time


class PingCommand(commands.Cog):
    """
    A simple ping command that says Pong! when executed.
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        before = time.monotonic()
        message = await ctx.send(embed=statics.get_embed('Pong!'))
        delta: int = round((time.monotonic() - before) * 1000)
        await message.edit(embed=statics.get_embed(f'Pong! `{delta} ms`'))


def setup(bot: commands.Bot):
    bot.add_cog(PingCommand(bot))
