import discord
import requests
import json
import random


def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

def get_motivation():
   response = requests.get('https://raw.githubusercontent.com/mubaris/motivate/master/200.json')
   quotes = json.loads(response.text)
   random_quote = random.choice(quotes['data'])
   return f'"{random_quote["quote"]}"\n\t--{random_quote["author"]}'

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message): 
    if message.author == self.user:
        return

    if message.content.startswith('$meme'):
        await message.channel.send(get_meme()) 
    
    if message.content.startswith('$motivation'):
        await message.channel.send(get_motivation()) 

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('DISCORD TOKEN')