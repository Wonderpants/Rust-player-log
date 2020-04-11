import asyncio

import valve.source
import valve.source.a2s
import valve.source.master_server
from discord import Webhook, RequestsWebhookAdapter

webhook = Webhook.partial(698337438677991465, 'gVUlHzwt1KXjw-dGaI88_S7V3dhxZr6rxQOb-2AMrA3VYZE7iTvSq651TmLTAxVe8Ck8', adapter=RequestsWebhookAdapter())

wanted = [
    "Таныоусхка",
    "BiGuMiG"
]

address = ('51.75.231.96', 28015)


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
                            webhook.send(f"{player} joined.", username="{player_count}/{max_players} {server_name}".format(**info), avatar_url='https://www.gamegrin.com/assets/games/rust/primary-image/rustlogo.jpg')
                    for player in playersFound:
                        if player not in players:
                            webhook.send(f"{player} left.", username="{player_count}/{max_players} {server_name}".format(**info), avatar_url='https://www.gamegrin.com/assets/games/rust/primary-image/rustlogo.jpg')
                playersFound = players
        except Exception as error:
            print(error)
        await asyncio.sleep(10)


loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()
