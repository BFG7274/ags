from pkg.log import log
from telethon import TelegramClient
from pkg.config import conf


def main():
    client = TelegramClient(
        'anon', conf['telegram']['api_id'], conf['telegram']['api_hash'])
    with client:
        client.run_until_disconnected()


def __init__():
    log.INFO("AGS Starting ...")


if __name__ == '__main__':
    main()
