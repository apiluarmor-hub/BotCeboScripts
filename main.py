import discord
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()

GUILD_ID = 1480009880105517069

class MyClient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        guild = discord.Object(id=GUILD_ID)
        self.tree.copy_global_to(guild=guild)
        synced = await self.tree.sync(guild=guild)
        print(f"✅ Sync OK: {len(synced)} comandos")

client = MyClient()

@client.event
async def on_ready():
    print(f"BOT: {client.user}")
    print("SERVIDORES:")

    for g in client.guilds:
        print(f"- {g.name} | {g.id}")

@client.tree.command(
    name="hablar",
    description="Envía un mensaje",
    guild=discord.Object(id=GUILD_ID)
)
async def hablar(interaction: discord.Interaction, texto: str):
    await interaction.response.send_message("✅ enviado", ephemeral=True)
    await interaction.channel.send(texto)

client.run(os.getenv("DISCORD_TOKEN"))
