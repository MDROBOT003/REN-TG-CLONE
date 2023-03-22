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
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQCL5kfkD16eVaR5puifLWuaePPI4rTyShZOima5K91wIcSmNMqhsSMu0kO7xIUEoL0b_6iTyh_0M6QqVooqYBTLVB6DBb0vXUQurV88McKQwr4xoHrTlmRMo1mi5-LYHUnBo6iozVOWEte5mUiEyll2hV4ZhUZxZ9GiDsTmg1oV6koJuuMI_u0SGVPg_hSZVlq_xX0KonU40O_eS69GqtMtkGuzvF9JjTRx6s0Hgm7PBFoqN_uaAn-jtVJ0-cznsDV9DmRZOcxaBkuFx6R1jt1XVL7AuPPcJfzBXaRDxqO1cMC1tVhO55434zFOdzIAE550zarwuOcSzqTi_hODCHDLaYcCeAA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgres://fileforward_xgrl_user:kkmQxLQoxea8Y6h2AnFaM80ege5Yv6Dd@dpg-cgcsbo64dad6fr6t3k6g-a/fileforward_xgrl")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
