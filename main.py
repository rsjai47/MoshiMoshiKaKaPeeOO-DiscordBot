import os
import discord
import random
import ascii
from keep_me_alive import keep_me_alive



client = discord.Client()

Greetings = ["Sup Nigga!","Wassup Nigga","Oombu","Sup Simp","Gotha yenna","Sollra Baadu","Time illa","Nani sempai","konichiwa sempai!","Oniii-chan","Yare Yare","Ora Ora","Mada Mada Mada","Ara Ara"]
mikasa = ['mikasa.png','download.jpg']

@client.event
async def on_ready():
  print('logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return 
  
  msg = message.content

  if msg == '!m':
    await message.channel.send(content = random.choice(Greetings),tts = bool(random.getrandbits(1)))

  if msg.startswith('!m mikasa'):
    await message.channel.send(file=discord.File(random.choice(mikasa)))

  if msg.startswith('!m ascii'):
    nw = 130
    if msg.startswith('!m ascii1'):
      nw = 100
    if msg.startswith('!m ascii2'):
      nw = 130
    if msg.startswith('!m ascii3'):
      nw = 200
    
    print("number " + str(nw))
    print(message.attachments[0].url)
    ascii.image_url = message.attachments[0].url
    print("image url ===== "+ascii.image_url)
    ascii.ascii(nw)
    await message.channel.send(file=discord.File('ascii_image.txt'))
  
  if msg.startswith('!m help'):
      print("lol")
      embedVar = discord.Embed(title="MoshiMoshiKaKaPeeOO", description="Happy weeb life", color=0x000000)
      embedVar.add_field(name="!m", value="something to make u feel at home", inline=False)
      embedVar.add_field(name="!m mikasa", value="👺", inline=False)
      embedVar.add_field(name="!m ascii", value="ascii art 🤓", inline=False)
      await message.channel.send(embed=embedVar)


    

keep_me_alive()
token = os.environ['TOKEN']
client.run(token)
