#Game Bot
import random, os, discord
from dotenv import load_dotenv
from datetime import datetime
from discord.ext import commands


load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('Discord_GUILD')








#Discord    
client = discord.Client()
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}'
    )




def roshambo(user_choice):
    global computer
    global player
    #Trys roshambo split and return meme if wrong
    try:
        response = ('Its a tie!', 'You win!', 'You lose!') 
    except:
        return "SoMeThInG wEnT wRoNg"

    choices = ('Rock', 'Paper', 'Scissors')
    computer = random.choice(choices)
    player = user_choice.split('$Roshambo',1)[1].strip()

    #Main Game Block
    if player == 'Rock' and computer == 'Rock':
        return response[0]
    elif player == 'Rock' and computer == 'Paper':
        return response[2]
    elif player == 'Rock' and computer == 'Scissors':
        return response[1]
    elif player == 'Paper' and computer == 'Rock':
        return response[1]
    elif player == 'Paper' and computer == 'Paper':
        return response[0]
    elif player == 'Paper' and computer == 'Scissors':
        return response[2]
    elif player == 'Scissors' and computer == 'Rock':
        return response[2]
    elif player == 'Scissors' and computer == 'Paper':
        return response[1]
    elif player == 'Scissors' and computer == 'Scissors':
        return response[0]
    else:
        return 'Something Went wrong!'
    


bot = commands.Bot(command_prefix='$')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '$Roshambo Help':
        await message.channel.send('Type $Roshambo Rock, $Roshambo Paper, or $Roshambo Scissors to Play Rock, Paper Scissors')
        
    elif message.content.startswith('$Roshambo'):
        game = roshambo(message.content)
        await message.channel.send('you chose: ' + player +' and I chose: '+ computer + ' so... ' + game)
    


client.run(TOKEN)
