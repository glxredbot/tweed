from .commands import Commands


def setup(bot):
    bot.add_cog(commands())
