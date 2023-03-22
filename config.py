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
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQBtrbtdN4h_3YgsulfyrluM0xJzOPbM54wXQYLUVGqd-gohi_JEHRfMV-mGPY3dEqjQhJdZpUPxXWgLrQmhok9ZvwlPFpWn878YfhTdL0vO3U8cbkmwesGRamhmzm0f_8SLK43IAMRxaogt5yXP1o7IU-Jjz3wolK10uO2d_PFIzAgcvn1ASVHUinTbRstfC5bN2SBZSQMvHqhxslZnf0EeMfG_VGtPnEB2MriATz9YUPyp1DXyDWTH92tC--HFtQvxz3Xb6MFVPuUpsk9AgIJQ2fied95z_9Apuebi5gROcBY-7eKzsPIwJBdP36-DOK3yO2A_m0BJncw6AlJezSLyaYcCeAA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgres://fileforward_xgrl_user:kkmQxLQoxea8Y6h2AnFaM80ege5Yv6Dd@dpg-cgcsbo64dad6fr6t3k6g-a/fileforward_xgrl")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
