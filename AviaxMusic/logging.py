import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler(),
    ],
)

logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.CRITICAL)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)
logging.getLogger("pymongo").setLevel(logging.CRITICAL)
logging.getLogger("yt-dlp").setLevel(logging.ERROR)
logging.getLogger("asyncio").setLevel(logging.CRITICAL)



def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
