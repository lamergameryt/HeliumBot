from discord.ext import commands
import requests
import statics

CAT_API = 'https://aws.random.cat/meow'
DOG_API = 'https://dog.ceo/api/breeds/image/random'


class Animals(commands.Cog, name='animals'):
    """
    Fulfil your inner animal fetish.
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(
        brief='Meow meow... meow.',
        help='Get a random image / gif related to a cat (can be a meme too)'
    )
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cat(self, ctx: commands.Context):
        response = requests.get(CAT_API).json()
        await ctx.send(embed=statics.get_embed('Here is a random cat for you', 'Random Cat')
                       .set_image(url=response['file']))

    @commands.command(
        brief='Woof woof... bark.',
        help='Get a random image / gif of a dog.'
    )
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dog(self, ctx: commands.Context):
        response = requests.get(DOG_API).json()
        await ctx.send(embed=statics.get_embed('Here is a random dog for you.', 'Random dog')
                       .set_image(url=response['message']))


def setup(bot: commands.Bot):
    bot.add_cog(Animals(bot))
