#bot.py
import hikari
import lightbulb
import requests
import os
from threading import Thread

from dotenv import load_dotenv
load_dotenv()

#bot status http server based on https://gist.github.com/kwk/5387c0e8d629d09f93665169879ccb86
from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message = "Random Owen WOWson is running."
        self.wfile.write(bytes(message, "utf8"))

server = HTTPServer(('localhost', 8000), handler)

def serve_forever(s):
    with s:
        s.serve_forever()

status_server_thread = Thread(target=serve_forever, args=(server,))
status_server_thread.start()

#discord bot powered by hikari and lightbulb
bot = lightbulb.BotApp(
    token=os.getenv('TOKEN'),
    default_enabled_guilds=(405243613073637377)
)

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('RandomOwenWOWson started.')

@bot.command
@lightbulb.command('wow', 'Send a random Owen Wilson "wow" clip')
@lightbulb.implements(lightbulb.SlashCommand)
async def wow(ctx):
    response = requests.get("https://owen-wilson-wow-api.herokuapp.com/wows/random")
    if response.status_code == 200:
        data = response.json()[0]
        print(f'{ctx.member.display_name} issued {data["video"]["720p"]}')
        await ctx.respond(f'Owen WOWson says, "wao" in {data["movie"]}:\n{data["video"]["720p"]}')
    else:
        embed = (
            hikari.Embed(
                colour=0xF1C232,
            )
            .set_image("https://c.tenor.com/lekaAGbLIA8AAAAC/wao-wow.gif")
        )
        print(f'{ctx.member.display_name} issued https://c.tenor.com/lekaAGbLIA8AAAAC/wao-wow.gif')
        await ctx.respond(embed)

bot.run()