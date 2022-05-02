from fileinput import filename
import hikari
import lightbulb
import requests

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