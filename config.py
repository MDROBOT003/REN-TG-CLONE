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
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQCWNWIAmasjHdLBFoJ3m2uJqjeMOtS3CbtlnNt7zsY-3oOhjBeBBz9T0XrKSc7jKuj5Lju5ccAs8sxpPgRLRMUlzsRqLqNLJjqRgsFjsCe6Cug8gA96f9vxlLSpo2EYHJ76kXKfdS3z-gVy1tavpdBCVFr3hMvcwUZvVieoWJl999S9OReAsiRK_BU7zdes8qHUtKihrNtYnAJN6uCvQMwpFEi1wQn6Hjjh1V8V1pRYiIZ3MYw98Vy_Ww2m12WhkLRDr8I36T_Ib2ItPv9F-IB37D0JMMXTzb6turj2ZU5HxERdPrzxeEoflaZPl08v6VnJggtv09FHEeISUXn4-X3ayUSjzAAAAABphwJ4AA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgres://fileforward_xgrl_user:kkmQxLQoxea8Y6h2AnFaM80ege5Yv6Dd@dpg-cgcsbo64dad6fr6t3k6g-a.oregon-postgres.render.com/fileforward_xgrl")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
