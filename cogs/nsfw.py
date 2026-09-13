from discord.ext import commands
from modules import apicall


class Nsfw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # HENTAI
    @commands.command()
    async def waifu_hentai(self, ctx):
        if not ctx.channel.is_nsfw():
            await ctx.send("Commande utilisable uniquement dans un salon NSFW.")
            return

        id, image = apicall.waifuapi_nsfw("hentai")
        await ctx.send(f"{image}\nID = {id}")

    # ERO
    @commands.command()
    async def waifu_ero(self, ctx):
        if not ctx.channel.is_nsfw():
            await ctx.send("Commande utilisable uniquement dans un salon NSFW.")
            return

        id, image = apicall.waifuapi_nsfw("ero")
        await ctx.send(f"{image}\nID = {id}")

    # ASS
    @commands.command()
    async def waifu_ass(self, ctx):
        if not ctx.channel.is_nsfw():
            await ctx.send("Commande utilisable uniquement dans un salon NSFW.")
            return

        id, image = apicall.waifuapi_nsfw("ass")
        await ctx.send(f"{image}\nID = {id}")

    # MILF
    @commands.command()
    async def waifu_milf(self, ctx):
        if not ctx.channel.is_nsfw():
            await ctx.send("Commande utilisable uniquement dans un salon NSFW.")
            return

        id, image = apicall.waifuapi_nsfw("milf")
        await ctx.send(f"{image}\nID = {id}")

    # ORAL
    @commands.command()
    async def waifu_oral(self, ctx):
        if not ctx.channel.is_nsfw():
            await ctx.send("Commande utilisable uniquement dans un salon NSFW.")
            return

        id, image = apicall.waifuapi_nsfw("oral")
        await ctx.send(f"{image}\nID = {id}")

    # PAIZURI
    @commands.command()
    async def waifu_paizuri(self, ctx):
        if not ctx.channel.is_nsfw():
            await ctx.send("Commande utilisable uniquement dans un salon NSFW.")
            return

        id, image = apicall.waifuapi_nsfw("paizuri")
        await ctx.send(f"{image}\nID = {id}")

    # ECCHI
    @commands.command()
    async def waifu_ecchi(self, ctx):
        if not ctx.channel.is_nsfw():
            await ctx.send("Commande utilisable uniquement dans un salon NSFW.")
            return

        id, image = apicall.waifuapi_nsfw("ecchi")
        await ctx.send(f"{image}\nID = {id}")


async def setup(bot):
    await bot.add_cog(Nsfw(bot))
