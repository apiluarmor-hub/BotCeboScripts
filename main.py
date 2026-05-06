import discord
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

GUILD_ID = 1480009881758077066  # ← tu servidor

@client.event
async def on_ready():
    print(f'✅ Bot conectado como {client.user}')
    
    guild = discord.Object(id=GUILD_ID)
    
    try:
        await tree.copy_global_to(guild=guild)
        synced = await tree.sync(guild=guild)
        print(f'✅ Comandos sincronizados: {len(synced)}')
    except Exception as e:
        print(e)

@tree.command(
    name="hablar", 
    description="El bot envía tu mensaje en público",
    guild=discord.Object(id=GUILD_ID)  # 👈 importante
)
@app_commands.describe(texto="Mensaje que quieres que el bot envíe")
async def hablar(interaction: discord.Interaction, texto: str):
    
    # 👁️ Confirmación privada
    await interaction.response.send_message("✅ Mensaje enviado", ephemeral=True)
    
    # 🌍 Mensaje público
    await interaction.channel.send(texto)

client.run(os.getenv("DISCORD_TOKEN"))
