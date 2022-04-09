import discord
from discord import Message

from graph import Pyasciigraph

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message: Message):
    if message.author == client.user:
        return

    mentions_me = False
    for member in message.mentions:
        if member.id == client.user.id:
            mentions_me = True

    if mentions_me and message.reference:
        replied_msg: Message = await message.channel.fetch_message(
            message.reference.message_id)
        print(replied_msg.reactions)
        data = list(map(lambda x: (x.emoji, x.count), replied_msg.reactions))
        print(data)

        pyasciigraph = Pyasciigraph()
        graph = pyasciigraph.graph(None, data)
        await message.reply("```" + "\n".join(graph) + "```")

client.run('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
