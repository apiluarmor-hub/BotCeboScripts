import discord
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

GUILD_ID = 1480009881758077066 # ← Cambia esto con tu ID de servidor

@client.event
async def on_ready():
    print(f'✅ Bot conectado como {client.user}')
    
    guild = discord.Object(id=GUILD_ID)
    await tree.copy_global_to(guild=guild)
    synced = await tree.sync(guild=guild)
    print(f'✅ Comandos sincronizados: {len(synced)}')

@tree.command(
    name="hablar", 
    description="El bot repite tu mensaje (solo tú lo ves)"
)
@app_commands.describe(texto="Mensaje que quieres que repita")
async def hablar(interaction: discord.Interaction, texto: str):
    await interaction.response.send_message(texto, ephemeral=True)

client.run(os.getenv("DISCORD_TOKEN"))
