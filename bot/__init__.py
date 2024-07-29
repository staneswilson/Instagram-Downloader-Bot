from instagrapi import Client as InstaClient
from instagrapi.exceptions import LoginRequired
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

# insta = InstaClient()
# if username and password:
#     try:
#         insta.login(username, password)
#     except Exception as e:
#         LOGGER.warn(f"Failed to login: {e}")
# else:
#     try:
#         insta.login_by_sessionid(session)
#     except Exception as e:
#         LOGGER.warn(f"Failed to login by session id: {e}")
#         os._exit(1)

insta = InstaClient()
def login_user():
    """
    Attempts to login to Instagram using either the provided session information
    or the provided username and password.
    """
    
    session = insta.load_settings(os.path.join(os.getcwd(), "session.json"))

    login_via_session = False
    login_via_pw = False

    if session:
        try:
            insta.set_settings(session)
            insta.login(username, password)

            # check if session is valid
            try:
                insta.get_timeline_feed()
            except LoginRequired:
                LOGGER.info("Session is invalid, need to login via username and password")

                old_session = insta.get_settings()

                # use the same device uuids across logins
                insta.set_settings({})
                insta.set_uuids(old_session["uuids"])

                insta.login(username, password)
            login_via_session = True
        except Exception as e:
            LOGGER.info("Couldn't login user using session information: %s" % e)

    if not login_via_session:
        try:
            LOGGER.info("Attempting to login via username and password. username: %s" % username)
            if insta.login(username, password):
                login_via_pw = True
        except Exception as e:
            LOGGER.info("Couldn't login user using username and password: %s" % e)

    if not login_via_pw and not login_via_session:
        raise Exception("Couldn't login user with either password or session")

login_user()

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