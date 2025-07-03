# SA Public Holiday Notifier

## Reason for Creating This

> The last time I kept track of public holidays was during my school and college years — you know, when it really mattered.
>
> Unfortunately, once I began working, I started forgetting these important days, to the point where I needed to be reminded by friends and family.
>
> So, as an early sign of “calendar amnesia,” I decided to create a simple Discord bot that sends a message to my Discord server whenever today is a public holiday.

---

## Dependencies

1. Uses [`discord.py`](https://discordpy.readthedocs.io/en/stable/) for sending messages via a Discord bot.
2. See `requirements.txt` in the project root for exact versions.

---

## Setting Up the Development Environment

### Prerequisites

1. A [Discord](https://discord.com/) account.
2. Basic understanding of setting up a Discord bot and adding it to a server.
3. Python installed on your machine.

#### Tested Versions

- Python: `v3.10.12`
- pip: `v22.0.2`

---

## 🚀 Setup Steps
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
