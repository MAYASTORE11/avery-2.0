import discord
from discord import client
from discord.ext import commands

class Bot:

    def __init__(self, token, vc):
        self.client = commands.Bot(command_prefix=';')
        self.token = token
        self.vc = vc

    @client.command()
    async def play(self, ctx, url: str):
        channel = discord.utils.get(ctx.guild.voice_channels, name=self.vc)
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        await channel.connect()

    @client.event
    async def on_ready():
        print('bot ready!')

    def run(self):
        self.client.run(self.token)


Bot('MTE4MTE5MTg0MjQzMjI4Njc3MA.G76PA2.0WL8MtPxSyNmM-AB25aZdm4yVc6fuO73-EsZUY', 'General').run()
