from redbot.core import commands
import discord


class Commands(commands.Cog):
    """custom commands"""

    @commands.command()
    async def mycom(self, ctx):
        @client.event
        async def on_message(message):
            if message.author == client.user:
                returns

            if message.content.startswith("?jiggle"):
                msg = "test".format(message)
                await client.send_message(message.channel, msg)



@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")
