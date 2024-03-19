import discord
from discord.ext import commands
from nba_predict import predict_linear_regression, predict_logistic_regression, predict_random_forest
import os
import certifi

# Set up environment for SSL certificates
os.environ['SSL_CERT_FILE'] = certifi.where()

# Setting up intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Initializing the bot with intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

# ... [Rest of your bot's commands]
@bot.command(name='predict')
async def predict(ctx):
    # Ask for the player's stage
    await ctx.send("Input the player's stage [young, prime, other]:")
    stage_msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author)

    # Ask for the player's full name
    await ctx.send("Enter the player's full name:")
    name_msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author)

    # Ask for the opponent team
    await ctx.send("Enter the opponent team abbreviation (e.g., 'NYK' for New York Knicks):")
    team_msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author)

    # Ask for the score threshold
    await ctx.send("Enter the score threshold:")
    score_msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author)

    try:
        player_stage = stage_msg.content.lower()
        player_name = name_msg.content
        opponent_team = team_msg.content.upper()
        score_threshold = float(score_msg.content)

        if player_stage == 'young':
            response = predict_linear_regression(player_name, opponent_team, score_threshold)
        elif player_stage == 'prime':
            response = predict_logistic_regression(player_name, opponent_team, score_threshold)
        else:  # Assuming 'other' or any other stage uses Random Forest
            response = predict_random_forest(player_name, opponent_team, score_threshold)

        await ctx.send(response)
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

@bot.command(name='shutdown')
async def shutdown(ctx):
    if ctx.author.id == 539583110556155954:  # Replace YOUR_USER_ID with your Discord user ID
        await ctx.send("Shutting down...")
        await bot.close()
    else:
        await ctx.send("You do not have permission to shut down the bot.")
# Run the bot with your token
bot.run('MTIwMTY0MTExMzAwNjY0OTM5NA.GB1aUm.aIjPyRSvqfdhwr8HdsvaJNTbG3bN_otjestm5s')
