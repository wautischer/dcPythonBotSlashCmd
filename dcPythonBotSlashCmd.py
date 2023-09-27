import interactions
import random

GandalfQuotes = []
GandalfQuotes.append('"I Did Not Pass Through Fire And Death To Bandy Crooked Words With A Witless Worm."')
GandalfQuotes.append('"Don\'t Tempt Me Frodo."')
GandalfQuotes.append('"There Never Was Much Hope. Just A Fool\'s Hope."')
GandalfQuotes.append('"Do Not Be Too Eager To Deal Out Death In Judgment. Even The Very Wise Cannot See All Ends."')
GandalfQuotes.append('"All We Have To Decide Is What To Do With The Time That Is Given To Us."')
GandalfQuotes.append('"Fly, You Fools!"')
GandalfQuotes.append('"I Will Not Say \'Do Not Weep\' Because Not All Tears Are Evil"')
GandalfQuotes.append('"Death Is Just Another Path, One That We All Must Take."')
GandalfQuotes.append('"A Wizard Is Never Late, Frodo Baggins. Nor Is He Early. He Arrives Precisely When He Means To."')
GandalfQuotes.append('"You Shall Not Pass!"')

GandalfSelfie = 'https://i.kym-cdn.com/entries/icons/original/000/042/690/Screen_Shot_2022-11-16_at_2.24.03_PM.jpg'

bot = interactions.Client(token="") #enter your token


@interactions.slash_command(
    name="hello",
    description="Say hi to Gandalf",
    scopes=[], #enter your server-id or leave it as is
)
async def hello(ctx: interactions.SlashContext):
    await ctx.send("Hi there!")


@interactions.slash_command(
    name="roll",
    description="Roll a number",
    scopes=[],
)
async def roll(ctx: interactions.SlashContext):
    await ctx.send(str(random.randint(1, 24000)))


@interactions.slash_command(
    name="dailymessage",
    description="Selfie from Gandalf",
    scopes=[],
)
async def dailymessage(ctx: interactions.SlashContext):
    await ctx.send(GandalfSelfie)


@interactions.slash_command(
    name="quote",
    description="Get a quote from Gandalf",
    scopes=[],
)
async def quote(ctx: interactions.SlashContext):
    quote = GandalfQuotes[int(random.randint(0, 10))]
    await ctx.send('*' + quote + '*')


@interactions.slash_command(
    name="help",
    description="Get info about bot functions",
    scopes=[],
)
async def help(ctx: interactions.SlashContext):
    await ctx.send('***/hello*** **`Say hello to the almighty Gandalf the White.`** ' \
                   '\n***/roll*** **`The great Gandalf the White chooses a number between 1 and 24,000.`**' \
                   '\n***/quote*** **`Gandalf the White will tell you one of his quotes.`**' \
                   '\n***/dailymessage*** **`Gandalf the White posts a selfie.`**')


bot.start()
