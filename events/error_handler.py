from discord.ext import commands


class ErrorHandler(commands.Cog):
    """
    This class is used to handle all the global level errors that may occur.
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # Ignore the errors of the command isn't found or user entered something invalid.
        ignored = (commands.CommandNotFound, commands.UserInputError)

        if isinstance(error, ignored):
            return

        if isinstance(error, commands.CommandOnCooldown):
            # The command is on cooldown.
            m, s = divmod(error.retry_after, 60)
            h, m = divmod(m, 60)
            if int(h) == 0 and int(m) == 0:
                await ctx.send(f' You must wait {int(s)} seconds to use this command!')
            elif int(h) == 0 and int(m) != 0:
                await ctx.send(f' You must wait {int(m)} minutes and {int(s)} seconds to use this command!')
            else:
                await ctx.send(
                    f' You must wait {int(h)} hours, {int(m)} minutes and {int(s)} seconds to use this command!')
        elif isinstance(error, commands.CheckFailure):
            # The user doesn't have the required permissions to use this command.
            await ctx.send("Hey! You lack permission to use this command.")
        else:
            raise error


def setup(bot: commands.Bot):
    bot.add_cog(ErrorHandler(bot))
