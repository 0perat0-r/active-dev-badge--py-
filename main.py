import discord
from discord.ext import commands
from discord import app_commands

bot = commands.Bot(
    command_prefix="!",
    intents=discord.Intents.all(),
    case_insensitive=True
)

@bot.command(name="sync")
async def sync(ctx):
    synced = await bot.tree.sync()
    await ctx.reply(f"Synced {len(synced)}")

@bot.tree.command(name="badge", description="Get your active developer badge.")
async def basge(interaction: discord.Interaction):
    await interaction.response.send_message("Claim your badge at <https://discord.com/developers/active-developer> after 24 ~ 48 hours.")

bot.run("YOUR_TOKEN")