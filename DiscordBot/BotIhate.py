import nextcord
from nextcord import Integration
from nextcord.ext import commands
import os
import Config
import datetime
import json



Intents = nextcord.Intents.default()
Intents.members = True
Intents.message_content = True

client = commands.Bot(intents=Intents)

@client.event
async def on_ready():
  print('Bot is online and is responding to incoming requests')



#@client.slash_command(name="ping", description="Pong!", guild_ids=[Config.guild_id])
#async def ping(interaction: nextcord.Interaction):
#  await interaction.response.send_message("Pong!")

@client.slash_command(name="find_a_player", description="Find a player", guild_ids=[Config.guild_id])
async def findaplayer(interaction: nextcord.Interaction, player: str):
  with open("Players.json", "r") as f:
    players = json.load(f)
  for P in players:
    if P["Username"] == player:
      del P["steam"]
      embed = nextcord.Embed(
        title=P["Username"],
        
      )
      await interaction.response.send_message(f"{P}")
  await interaction.response.send_message("Test!")
  


def run():
  client.run(Config.Discord_Token)