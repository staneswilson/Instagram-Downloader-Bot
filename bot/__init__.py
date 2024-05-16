from instagrapi import Client as Instaclient
from swibots import Client, BotCommand
import os
import logging
from dotenv import load_dotenv

LOGGER = logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

load_dotenv("config.env")

#instagram
username = os.getenv("user_name")
password = os.getenv("password")
session = os.getenv("session_id")

#Switch
bot_token = os.getenv("bot_token")
community = os.getenv("community_id")
community_url = os.getenv("community_url")
owner_id = os.getenv("owner_id")

folder = os.getenv("folder")

insta = Instaclient()
if username and password:
    try:
        insta.login(username, password)
    except Exception as e:
        LOGGER.warn(f"Failed to login: {e}")
else:
    try:
        insta.login_by_sessionid(session)
    except Exception as e:
        LOGGER.warn(f"Failed to login by session id: {e}")
        os._exit(1)

#Create a folder to store the downloaded files
if not os.path.isdir(folder):
    os.mkdir("downloads")

downloads = os.path.join(os.getcwd(), folder)

commands = [
    BotCommand("start", "Start the bot", True)
]

bot = Client(
    token=bot_token,
    plugins={'root': os.path.join(__package__, 'plugins')},
).set_bot_commands(commands)