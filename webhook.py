import os
import time
from discord_webhook import DiscordWebhook

webhook_url = os.environ["SLIMEY_HOOK"]

while True:
    DiscordWebhook(url=webhook_url, content='Time to code, you slacker!').execute()
    time.sleep(10)
    DiscordWebhook(url=webhook_url, content='Time to take a break perhaps?').execute()
    time.sleep(1)

