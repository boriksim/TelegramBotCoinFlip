import os
from dotenv import load_dotenv

load_dotenv()
import config

mode = config.MODE

if mode == "polling":
    os.system("python main_polling.py")
elif mode == "webhook":
    os.system("python main_webhook.py")
else:
    print("Error in MODE")
