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
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQCQIjipwlg4HK7BDjOx_WZyhLpqpcTYgkd--KUZDdhk2sCAPcbrStpEs-F54E1ZkFv8NtPlR_rBVljkRsaLMGTZzeC_2rPeNo4YCgXBLmgVBuX0NSdRy1a9YnGYmL3EHjPO8PsplF7NDUjAdBP7ob1N2mcCxVF0TobOwngTAG8W3VtmEu4WNbntY0-9Nhf93ysaHkYl7KZV1QhalgIsYkWC3qy0P-PtgjlMt6Z1Mm_rt3HtJ6ffuozdQm-SnhJiHUsthjMlTXcINOd--EABHMIBVVbxDv8Uq8G-L5x_SihVvQop9ZukxILM8L-DMna36LncC7NNjA8m3WsdmPIdhn-7aYcCeAA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgres://fileforward_xgrl_user:kkmQxLQoxea8Y6h2AnFaM80ege5Yv6Dd@dpg-cgcsbo64dad6fr6t3k6g-a/fileforward_xgrl")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
