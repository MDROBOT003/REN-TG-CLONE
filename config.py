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
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQAj1MsAhWRzj_afvvsTsR7V8vPvd23vH1jDxquKCeU57AJ9NVugxxRIQBnrR7GpjsKoOBJol4mJOrwe9b2y6IVhLFhrBWyT4I9sN0tDljpYFarnl1UiCf8Zb6djkxePtNlAqOWVTo7uFFoJVNp8-CUrSK7iFrbQg-AMtuCuM4qWawnSHbRQjfU9MIyQnmzofvNU9QEWDgu_T2BPCIoN3lqCFfehM0t1hGnd6TcxqCVzrQ0HHBlELc0Wsz-xdMzLG8EGC9vuI_4HIC9qL1pd1o7tkVBI_14H33kcjNiuteLGQvwuxFMf-txtJuN9yurTer3x9DpjDXmaTGyrMUZ9aVMPk85BfAAAAAFXJcKtAQ")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgres://fileforward_xgrl_user:kkmQxLQoxea8Y6h2AnFaM80ege5Yv6Dd@dpg-cgcsbo64dad6fr6t3k6g-a/fileforward_xgrl")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
