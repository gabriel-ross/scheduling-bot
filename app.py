from api_keys import DISCORD_BOT_KEY
from discord_event_handler import DiscordClient

if __name__ == '__main__':
    client = DiscordClient()
    client.run(DISCORD_BOT_KEY)