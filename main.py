import discord
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

GUILD_ID = 1480009880105517069

@client.event
async def on_ready():
    print(f'✅ Bot conectado como {client.user}')
    
    try:
        synced = await tree.sync(guild=discord.Object(id=GUILD_ID))
        print(f'✅ Comandos sincronizados: {len(synced)}')
    except Exception as e:
        print(f'❌ Error sync: {e}')

@tree.command(
    name="hablar",
    description="El bot envía tu mensaje",
    guild=discord.Object(id=GUILD_ID)
)
@app_commands.describe(texto="Mensaje")
async def hablar(interaction: discord.Interaction, texto: str):
    await interaction.response.send_message("✅ enviado", ephemeral=True)
    await interaction.channel.send(texto)

client.run(os.getenv("DISCORD_TOKEN"))
