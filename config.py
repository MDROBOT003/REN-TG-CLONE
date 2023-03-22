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
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "1BVtsOHYBu280uIV9rEwDTwVqL4JxHqBtua0E4ctjyu51KOgXXqZTGS0ou45mfY6_EdM6IEZkz-K_5B63Hl8D9dlq7c3-HU3I-rFzqHzoIY6EYsMg2LNDs92DofKM358X5i_dSrw1eoSQPCbuNS7EreQpyJaeBKGgrWFJG-j4j3ZC8Ccoa6iIkP3r4aM1Yvvgu7vij13gXbC8thdhcECaBPmL5MRARYMW6aigQAI36zCxdhHLf9USDnCqOtW7A4OR-pzRrvIGPZny967DNDs_FNnWMghLovVwJBOkkSb7LiW9sQLtxNLvUTiwjCzergQTWTg7MnliAptjAYhTrdMIjVv_BnIDenE=")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgres://fileforward_xgrl_user:kkmQxLQoxea8Y6h2AnFaM80ege5Yv6Dd@dpg-cgcsbo64dad6fr6t3k6g-a/fileforward_xgrl")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
