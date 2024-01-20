from typing import Final
import os
import discord
from dotenv import load_dotenv
from discord import Intents, Message
from discord import app_commands
from discord.ext import commands
from responses import get_response
import custom_commands

# Load token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# set up bot
intents: Intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


# message
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message empty because intents not enabled')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        responses: str = get_response(user_message)
        await message.author.send(responses) if is_private else await message.channel.send(responses)
    except Exception as e:
        print(e)


# handling startup
@bot.event
async def on_ready() -> None:
    print(f'{bot.user} is now running')
    try:
        synced = await bot.tree.sync()
        print(f"synced {len(synced)} command(s)")
    except Exception as e:
        print(f"synced error: {e}")


# handling incoming messages
@bot.event
async def on_message(message: Message) -> None:
    if message.author == bot.user:
        return
    user_massage: str = message.content

    # print(f'[{channel}] {username}:  "{user_massage}"')
    if 'delete' in message.content:
        await message.delete()
        print(f'Message deleted')
    else:
        await send_message(message, user_massage)


# commands
@bot.tree.command(name="test", description='This is the full description')
async def test(interaction: discord.Interaction):
    # await interaction.response.send_message("command")
    await interaction.response.send_message("hello world! This is a differnt command")


@bot.tree.command(name='clear', description='clears all messages from a channel')
async def clear(ctx):
    await custom_commands.clear_channel(ctx)


@bot.tree.command(name='shy', description=':point_right::point_left:')
async def shy(ctx):
    await custom_commands.shy(ctx)

# main entry pint
def main() -> None:
    bot.run(token=TOKEN)


if __name__ == '__main__':
    main()
