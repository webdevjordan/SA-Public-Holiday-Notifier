
# Import dependencies
import os
import discord
from datetime import datetime
from discord.ext import commands


# Set the discord credentials by fetching the env variables
TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = int(os.environ["CHANNEL_ID"])


#The format to adding a new holidays entry is as follows
# "MM-DD" : "Type of holiday"
PUBLIC_HOLIDAYS = {
    "01-01": "New Year's Day",
    "03-21": "Human Rights Day",
    "04-18": "Good Friday",
    "04-21": "Family Day",
    "04-27": "Freedom Day",
    "05-01": "Workers Day",
    "06-16": "Youth Day",
    "08-09": "National Womens Day",
    "09-24": "Heritage Day",
    "10-16": "Day of Reconciliation",
    "10-25": "Christmas Day",
    "10-26": "Day of Goodwill"
}


def get_holiday_message():
    """
    Return a message indicating whether today is a public holiday.
    """

    today = datetime.now().strftime('%m-%d')
    if today in PUBLIC_HOLIDAYS:
        message = f"Woohoo!!! Today is {PUBLIC_HOLIDAYS[today]} 🎉"
        day_name = datetime.now().strftime("%A")
        if day_name == "Sunday":
            message = f"{message}\nReminder that Monday is also a holiday"
        return message

    return "No holidays for today😞😭"



# Send a message to the discord channel using the bot
message = get_holiday_message()
if message:
    intents = discord.Intents.default()
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            await channel.send(message)
        await bot.close()

    bot.run(TOKEN)
