import os
import discord
import asyncio
from keep_alive import keep_alive
intents = discord.Intents.default()
intents.members = True

client=discord.Client(intents=intents)

@client.event
async def on_ready():
  print('logged in as')
  print(client.user.name)
  print(client.user.id)
  print('-----')

newUserMessage = """
-----------------------------------------------
Hey there! Welcome to the Post Keynesian Church. After reading the rules carefully, please answer these 3 vetting questions in <#853082972251750447> :

1.) Where did you find this place?
2.) What ideology/school of economics are you affiliated with? If none, pluralism is acceptable. 
3.) What is the title of the latest book you have read? 

Make sure to ping <<@&853096268167249930>> or <@!655039507053412364> or <@!886651845815197716> or <@!609514003579928598>
In addtion make sure you read <#853009735146274876> if you want to add sources
-----------------------------------------------
"""

@client.event
async def on_message(message):
    if message.content.startswith('$greet'):
        channel = message.channel
        await channel.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send('Hello {.author}!'.format(msg))

@client.event
async def on_member_join(member):
  print("Recognised that a member called " + member.name + " joined")
  channel = client.get_channel(853082972251750447) 
  await channel.send(newUserMessage)
  print("Sent message to " + member.name)
  #except:
  #  print("Couldn't message " + member.name)

keep_alive()

client.run(os.getenv("'Minsky'"))