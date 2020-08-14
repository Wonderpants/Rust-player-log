import asyncio

import valve.source
import valve.source.a2s
import valve.source.master_server
from discord import Webhook, RequestsWebhookAdapter, Embed, Colour
import traceback

webhook = Webhook.partial(743162532356685944, 'sDHqvKb5-7dEahZZQvwLo4_X-SKDq1AAyHpR5akwt1Ms4zKAYC4QEwe7Z_YUkaiRkhKd', adapter=RequestsWebhookAdapter())

wanted = [
    "Таныоусхка",
    "BiGuMiG"
]

address = ('164.132.207.225', 28015)

async def main():
    playersFound = []
    while True:
        print('1')
        try:
            with valve.source.a2s.ServerQuerier(address) as query:
                info = query.info()
                try:
                    players = [p['name'] for p in query.players()['players']]
                except Exception as error:
                    print(query.players())
                    continue
                if playersFound:
                    em = Embed(title="[EU] Corrosion PvE")
                    em.set_footer(text="{player_count}/{max_players}".format(**info) + f" - {int(query.ping())}ms")
                    for player in players:
                        if player not in playersFound:
                            em.colour = Colour.green()
                            em.description = f"{player} joined."
                            webhook.send(embed = em, username="{server_name}".format(**info), avatar_url='https://www.gamegrin.com/assets/games/rust/primary-image/rustlogo.jpg')
                            print(em.description)
                    for player in playersFound:
                        if player not in players:
                            em.colour = Colour.red()
                            em.description = f"{player} left."
                            webhook.send(embed = em, username="{server_name}".format(**info), avatar_url='https://www.gamegrin.com/assets/games/rust/primary-image/rustlogo.jpg')
                            print(em.description)
                playersFound = players
        except Exception as error:
            print('\n'.join(traceback.format_exception(type(error), error, error.__traceback__)))
        await asyncio.sleep(10)

loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()
