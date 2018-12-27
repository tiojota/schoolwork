import discord
import asyncio

client = discord.Client()


@client.event
async def on_ready():
    print('BOT ONLINE - OLÁ, MUNDO')
    print(client.user.name)
    print(client.user.id)
    print('-----PR------')

@client.event
async def on_message(message):
    if message.content.lower().startswith('ugabuga'):
        await client.send_message(message.channel, "uga buga uga buga uga buga uga buga")


client.run('NTI3ODU3NzI1ODQyMTI4OTMz.DwZ7dg.uq_IMZqwoGjUbM24_5WIxkHlF8s')
