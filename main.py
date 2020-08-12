import asyncio

import valve.source
import valve.source.a2s
import valve.source.master_server
from discord import Webhook, RequestsWebhookAdapter

webhook = Webhook.partial(743162532356685944, 'sDHqvKb5-7dEahZZQvwLo4_X-SKDq1AAyHpR5akwt1Ms4zKAYC4QEwe7Z_YUkaiRkhKd', adapter=RequestsWebhookAdapter())

wanted = [
    "Таныоусхка",
    "BiGuMiG"
]

address = ('164.132.207.225', 28015)


async def main():
    playersFound = []
    while True:
        try:
            with valve.source.a2s.ServerQuerier(address) as query:
                info = query.info()
                players = [p['name'] for p in query.players()['players']]
                if playersFound:
                    for player in players:
                        if player not in playersFound:
                            pass
                            webhook.send(f"{player} joined.", username="{player_count}/{max_players} {server_name}".format(**info), avatar_url='https://www.gamegrin.com/assets/games/rust/primary-image/rustlogo.jpg')
                    for player in playersFound:
                        if player not in players:
                            pass
                            webhook.send(f"{player} left.", username="{player_count}/{max_players} {server_name}".format(**info), avatar_url='https://www.gamegrin.com/assets/games/rust/primary-image/rustlogo.jpg')
                playersFound = players
        except Exception as error:
            print(error)
        await asyncio.sleep(10)


loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()
