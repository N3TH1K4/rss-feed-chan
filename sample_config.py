from os import environ

from dotenv import load_dotenv

load_dotenv("config.env")

HEROKU = bool(
    environ.get("DYNO")
)  # NOTE Make it false if you're not deploying on heroku or docker.

if HEROKU:

    BOT_TOKEN = environ.get("BOT_TOKEN", None)
    API_ID = int(environ.get("API_ID", 6))
    API_HASH = environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    SESSION_STRING = environ.get("SESSION_STRING", None)
    USERBOT_PREFIX = environ.get("USERBOT_PREFIX", ".")
    SUDO_USERS_ID = [int(x) for x in environ.get("SUDO_USERS_ID", "").split()]
    LOG_GROUP_ID = int(environ.get("LOG_GROUP_ID", None))
    GBAN_LOG_GROUP_ID = int(environ.get("GBAN_LOG_GROUP_ID", None))
    MESSAGE_DUMP_CHAT = int(environ.get("MESSAGE_DUMP_CHAT", None))
    WELCOME_DELAY_KICK_SEC = int(environ.get("WELCOME_DELAY_KICK_SEC", None))
    MONGO_URL = environ.get("MONGO_URL", None)
    ARQ_API_URL = environ.get("ARQ_API_URL", None)
    ARQ_API_KEY = environ.get("ARQ_API_KEY", None)
    LOG_MENTIONS = bool(int(environ.get("LOG_MENTIONS", None)))
    RSS_DELAY = int(environ.get("RSS_DELAY", None))
    PM_PERMIT = bool(int(environ.get("PM_PERMIT", None)))
else:
    BOT_TOKEN = "5588117391:AAGYNQNFoU1g_4nVFxp-4A7NsXsjbjKfiR8"
    API_ID = 18983092
    API_HASH = "a6005a70e88369b4fb08b8350ebbdd35"
    USERBOT_PREFIX = "."
    PHONE_NUMBER = "+94702539508"  # Need for Userbot
    SUDO_USERS_ID = [
        1930645496,
    ]  # Sudo users have full access to everything, don't trust anyone
    LOG_GROUP_ID = -1001549232084
    GBAN_LOG_GROUP_ID = -1001549232084
    MESSAGE_DUMP_CHAT = -1001549232084
    WELCOME_DELAY_KICK_SEC = 300
    MONGO_URL = "mongodb+srv://TROJ3N:Nethika123@cluster0.uppg6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    ARQ_API_KEY = "MHUNZH-XFGSYO-BFQSZR-HDTQGL-ARQ"
    ARQ_API_URL = "https://arq.hamker.in"
    LOG_MENTIONS = False
    RSS_DELAY = 300  # In seconds
    PM_PERMIT = True
