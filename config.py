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
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQAj1MsAnN6YPR1VOFSHMXl5WCwPJOpjMzwpRW7054TTUsYvopePx1sIx8XoRVSnRjwcVDgrFKeul-k9vJtjFFImYW3dGCLQzxX4l9SBVjfEZXdz0mF5069tYEbALzbVV2CeNQh4TlBzThzakTxEMFtHM_8fYmLIYFjWv2bMyeg_GUbO7WOzvk9hXnZ6TC67lLqwAQ483qT_0tYFk4W38lXm_2GuHMjG1OYac3skdSZeo3b1XDHVMtseaI1uLSJ5rBWzJDIpKZvPplC-NhgzEp0AVE4yzJJsRvDAAWwZKg_Qkpz36ng_g75I-_ewnv9A2yciF3vBAeu3Sg9g2RbnzjWt4_-iqAAAAAFXJcKtAQ")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgres://fileforward_xgrl_user:kkmQxLQoxea8Y6h2AnFaM80ege5Yv6Dd@dpg-cgcsbo64dad6fr6t3k6g-a.oregon-postgres.render.com/fileforward_xgrl")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
