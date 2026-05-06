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
    print(f"BOT: {client.user}")
    print("SERVIDORES DONDE ESTÁ EL BOT:")

    # 🔍 DEBUG REAL (esto es clave para tu error)
    for g in client.guilds:
        print(f"- {g.name} | {g.id}")

    # 🔄 SYNC SOLO AL GUILD
    try:
        guild = discord.Object(id=GUILD_ID)
        synced = await tree.sync(guild=guild)
        print(f"✅ Comandos sincronizados: {len(synced)}")
    except Exception as e:
        print(f"❌ Error sync: {e}")

@tree.command(
    name="hablar",
    description="El bot envía tu mensaje",
    guild=discord.Object(id=GUILD_ID)
)
@app_commands.describe(texto="Mensaje que quieres enviar")
async def hablar(interaction: discord.Interaction, texto: str):

    # 👁️ solo tú ves esto
    await interaction.response.send_message("✅ enviado", ephemeral=True)

    # 🌍 mensaje público del bot
    await interaction.channel.send(texto)

client.run(os.getenv("DISCORD_TOKEN"))
