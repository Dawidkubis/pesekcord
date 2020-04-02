#!/usr/bin/python3

import discord
from sys import argv

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('chodi pesek okolo...'):
		await message.channel.send('nedivej se na necho...')

client.run(argv[1])
