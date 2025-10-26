# Import dependencies
import os
import discord
import time
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
    "12-25": "Christmas Day",
    "12-26": "Day of Goodwill"
}


#The format to adding a new birtdays entry is as follows
# "MM-DD" : "Type of holiday"
IMPORTANT_BIRTHDAYS = {
    "01-02": "Jordan",
    "02-24": "Father",
    "04-06": "Third",
    "08-05": "Wife and Nummnumm",
    "11-04": "Mother",
    "12-10": "Sister",
    "27-10": "Eli",
}


def get_holiday_message(todays_date):
    """
    Return a message indicating whether today is a public holiday.
    """

    if todays_date in PUBLIC_HOLIDAYS:
        message = f"Woohoo!!! Today is {PUBLIC_HOLIDAYS[todays_date]} 🎉"
        day_name = datetime.now().strftime("%A")
        if day_name == "Sunday":
            message = f"{message}\nReminder that Monday is also a holiday."
        return message

    return "No holidays for today😞😭"


def get_birthday_message(todays_date):
    """
    Return a message indicating whether today is an important birthday
    """

    if todays_date in IMPORTANT_BIRTHDAYS:
        return f"It is {IMPORTANT_BIRTHDAYS[todays_date]}'s birthday. Wish them a lovely day🎉"

    return ""


def send_message_to_discord(message):
    """
    Send a message to the discord channel using the bot
    """
    intents = discord.Intents.default()
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            await channel.send(message)
        await bot.close()

    bot.run(TOKEN)


def main():
    """
    Handles all the main operations
    """

    # Get todays that in "M-D"
    todays_date = datetime.now().strftime('%m-%d')


    # Send out the holiday message
    holiday_message = get_holiday_message(todays_date)
    if holiday_message:
        send_message_to_discord(holiday_message)

    print('sleeping...')
    time.sleep(20)
    print('done...')

    # Send out the birthday message
    birthday_message = get_birthday_message(todays_date)
    if birthday_message:
        send_message_to_discord(birthday_message)


main()