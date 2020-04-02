#!/usr/bin/python3

import discord
from sys import argv

from parse import parse

client = discord.Client()

@client.event
async def on_connect():
    print(f'connected')

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content:
		await message.channel.send('nedivej se na necho...')

client.run(argv[1])
