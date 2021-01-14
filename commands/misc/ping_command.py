from discord.ext import commands
import statics


class PingCommand(commands.Cog):
    """
    A simple ping command that says Pong! when executed.
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(embed=statics.get_embed('Pong!'))


def setup(bot: commands.Bot):
    bot.add_cog(PingCommand(bot))
