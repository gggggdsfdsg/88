import discord
from discord import app_commands
from discord.ext import commands
import random

# Intents to enable members and message activities
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

# Create the bot client with command prefix and enable slash commands
bot = commands.Bot(command_prefix='/', intents=intents)

# Replace with your actual bot token
TOKEN = 'MTMwNjE5ODYyMzY1ODMxMTc0MA.GqN7cP.iUKtUaDQFgpvXWNFmMwc2drT--oP1zCFk2gmT0'

# Sync command tree when the bot is ready
@bot.event
async def on_ready():
    await bot.tree.sync()  # Sync the slash commands with Discord
    print(f'Bot connected as {bot.user}')

# Slash command for /mine with specific requirements
@bot.tree.command(name="mine", description="Generate a 5x5 grid with exactly 3 gems and a seed of 64 characters.")
async def mine(interaction: discord.Interaction, seed: str):
    # Ensure the seed has exactly 64 characters
    if len(seed) != 64:
        await interaction.response.send_message("The seed must be provided from Stake!.")
        return

    gems_count = 3  # Fixed gems count
    minefield = generate_minefield(gems_count, seed)
    
    if minefield is None:
        await interaction.response.send_message("An error occurred while generating the minefield.")
        return
    
    formatted_minefield = format_grid(minefield)
    response = f"**⚠️⚠️The seed must be changed after u start betting again!⚠️⚠️**\nWin!: 1.48X \nSeed: {seed}\n\n{formatted_minefield}"
    await interaction.response.send_message(response)

# Function to generate a minefield based on the number of gems and seed
def generate_minefield(gems_count, seed):
    random.seed(seed)
    grid_size = 5
    total_cells = grid_size * grid_size
    
    cells = ['💣'] * total_cells
    gem_positions = random.sample(range(total_cells), gems_count)
    
    for pos in gem_positions:
        cells[pos] = '💎'
    
    grid = [cells[i * grid_size:(i + 1) * grid_size] for i in range(grid_size)]
    return grid

# Format the grid for display
def format_grid(grid):
    return '\n'.join([' '.join(row) for row in grid])

# Run the bot
bot.run(TOKEN)

