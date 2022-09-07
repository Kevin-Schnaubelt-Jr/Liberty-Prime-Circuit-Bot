'''
Bot time.
'''
import random

from bot_config import bot_key, server_id, server_general_channel
from pick6 import play_pick_6

import nextcord
from nextcord import Interaction, Intents, SlashOption
from nextcord.ext import commands

from Calculations import circuit_builder
intents = nextcord.Intents.default()
intents.message_content = True








bot = commands.Bot(command_prefix='!', intents=intents)

#Say hello when bot comes online.
prime_join_list = [
'LIBERTY PRIME IS ONLINE.', 'ALL SYSTEMS NOMINAL.', 'WEAPONS: HOT.',
'''Voice module online. 
Audio functionality test initialized. 
Designation: Liberty Prime. 
Mission: the liberation of Anchorage, Alaska. 
Primary Targets: any and all Red Chinese invaders. 
Emergency Communist Acquisition Directive: immediate self destruct. 
Better dead, than Red.''',

]

@bot.event
async def on_ready():

    general_channel = bot.get_channel(server_general_channel)

    await general_channel.send(random.choice(prime_join_list).upper())



#Say command make
@bot.slash_command(name='say', description='Make Liberty Prime say something', guild_ids=[server_id])
async def say_func(interaction: Interaction, msg:str):
    await interaction.response.send_message(msg)


#Circuit calculator
@bot.slash_command(name='calc', description='Make Liberty Prime calc something', guild_ids=[server_id])
async def calc_func(interaction: Interaction, volt:int, series:str, parallel:str):
    circuit_1 = circuit_builder(volt, series, parallel)
    response_f_str = f'''
    Here are your results.
    -- VOLTAGE --
    {circuit_1.voltage['Voltage']}
    -- RESISTANCE ohms--
    {circuit_1.resistance['Resistance']}
    -- CURRENT mA--
    {circuit_1.current['Current']}
    '''
    await interaction.response.send_message(response_f_str)


#Play pick6
@bot.slash_command(name='pick6', description='Play Pick6! Input the number of times you would like to play, and how much money you got', guild_ids=[server_id])
async def pick6_func(interaction: Interaction, number_of_plays:int, balance:int):
    result = play_pick_6(number_of_plays, balance)
    pick_6_return = f'''
    Here are your results.
    Balance {result['balance']}
    Expenses {result['expenses']}
    Earnings {result['earnings']}
    '''

    await interaction.response.send_message(pick_6_return)

contacts_description = f'''
This is the description for the...
contacts slash command'''
@bot.slash_command(name='contacts', description=contacts_description)
async def contacts_func(interaction: Interaction, number: int = SlashOption(
        name="picker",
        choices={"one": 1, "two": 2, "three": 3},
    )):


    # await interaction.response.Slash
    await interaction.response.send_message('working')

bot.run(bot_key)


