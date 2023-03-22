#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5757059757:AAEvjvpv1gmn8xHGAONAiTEjEbN7OaHwka8")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "9844066"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "0d3f74056f1e60388d3317548799ee17")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQCWNWIAmNyqTWg-IlWwXYQzd4AUW_wpOLY6vr9SDEipXSNnyeockeTuh_Db2B0GVsiowwLNX5JOVBaR3mKRgKU6wFmViqmJNbATx-OfcS6-mwZFUF-Up0bl_UA94tnKWpwZ0_GKc6Zn7w9DorAHX3J6J1unDQoBkdcLRbXDk9HxbnBA5kdq3VrGI3wRAsLjQG9C-G_FoY3j53SC1LlyadcKuY5dkfLc4AjqHVP7rKumW7LBMHF0fDqPf0ChbkJcFURXc3DfUdkedC8GoAcIDLPmLdISBRta4hxTr2Kvkqz6fMcDHcAhhheDk5a87gVMw-tL4tZi6Lz-C0dSvWmseBxx4U9PcwAAAABphwJ4AA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgres://fileforward_xgrl_user:kkmQxLQoxea8Y6h2AnFaM80ege5Yv6Dd@dpg-cgcsbo64dad6fr6t3k6g-a/fileforward_xgrl")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
