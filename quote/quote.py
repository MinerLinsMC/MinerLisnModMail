import typing
import discord
from discord.ext import commands
from modmailtranslation import Translator, KeyNotFoundError


class QuotePlugin(commands.Cog):
    def __init__(self, bot):
        self.bot: discord.Client = bot
        self.db = bot.plugin_db.get_partition(self)
        self.i18n = Translator("")

    @commands.command(aliases=["q"])
    async def quote(self, ctx: commands.Context, channel: typing.Optional[discord.TextChannel], message_id: str):
        if not channel:
            channel = ctx.channel
        try:
            try:
                message = await channel.fetch_message(int(message_id))
            except discord.NotFound:
                await ctx.send(self.i18n.get("**MinerLins**: Message was not found!"))
                return
            except discord.Forbidden:
                await ctx.send(self.i18n.get("**Minerlins**: Forbidden!"))
                return
            except:
                await ctx.send(self.i18n.get("**MinerLins**: An unknown error has occured!"))
                return
        except KeyNotFoundError:
            await ctx.send("**MinerLins**: Seems like the command isn't localized for your language yet!")
            return


