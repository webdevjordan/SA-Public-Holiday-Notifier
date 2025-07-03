# SA-Public-Holiday-Notifier

## Reason for creating this
```py
"""
The last time I kept track of public holidays was during my schooling and college years, you know where it really mattered.

Unfortunately when I begun working, I started forgetting these important days, to a point where I needed to be reminded by friends and family of them.

As a result, of my early signs of dementia, I decided to create a simple discord bot that sends messages to my discord server, letting me know if today is public holiday or not
"""
```

## Dependecies
1. Currently utilizing the [discord.py](https://discordpy.readthedocs.io/en/stable/) to allow the bot to `send message`. 
2. You can have a look at the `requirements.txt` found within this directory for the versioning and other dependencies

## How to setup the dev environment

### Pre-requistes
1. You need a `discord` account.
2. You need to have an understanding on setting up the discord bot and how-to integrate it with your discord servers and channels.
3. You need to have python installed on your local machine

#### Python and Pip versions
1. PIP `v22.0.2`
2. Python3 `v3.10.12`

## Steps
1. **Clone** this repository
3. **CD** into `SA-Public-Holiday-Notifier`.
2. **Create** a virutal evironment `sudo python3 -m venv bot-env`.
3. **Activate** the virtual environment `source bot-env/bin/activate`.
4. **Install** project dependencies `pip install -r requirements.txt`.
5. **SET** the `BOT_TOKEN`  and `CHANNEL_ID` environment variables.
   - Note: On the `ubuntu` distro I used `export`.
   - Note: Make sure you captured the `BOT_TOKEN` and `CHANNEL_ID` from discord bot and app setup phase.
6. **RUN** the `main.py` script using example command `python3 main.py`.
7. **Confirm** that you get a message in your discord channel.
