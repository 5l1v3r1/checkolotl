import checkolotl.utils.discord.webhook as webhook
from checkolotl.settings import settings


def start():
    if settings.announcer.discord_webhook_url and settings.announcer.on_start.discord.enabled:
        webhook.start()
