import imp
from telethon import TelegramClient
from pkg.config import init as config_init


def main():
    conf = config_init()
    client = TelegramClient('anon', conf['api_id'], conf['api_hash'])
    client_run(client)


def client_run(client):
    with client:
        client.run_until_disconnected()


if __name__ == '__main__':
    main()
