
from telethon import TelegramClient
from pkg.config import conf


def main():
    client = TelegramClient(
        'anon', conf['telegram']['api_id'], conf['telegram']['api_hash'])
    with client:
        client.run_until_disconnected()

    


if __name__ == '__main__':
    main()
