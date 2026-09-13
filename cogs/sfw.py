from discord.ext import commands
from modules import apicall


class Sfw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # WAIFU
    @commands.command()
    async def waifu(self, ctx):
        id, image = apicall.waifuapi()
        await ctx.send(f"{image}\nID = {id}")

    # MAID
    @commands.command()
    async def waifu_maid(self, ctx):
        id, image = apicall.waifuapi_sfw_tag("maid")
        await ctx.send(f"{image}\nID = {id}")

    # WAIFU (tag)
    @commands.command()
    async def waifu_waifu(self, ctx):
        id, image = apicall.waifuapi_sfw_tag("waifu")
        await ctx.send(f"{image}\nID = {id}")

    # MARIN KITAGAWA
    @commands.command()
    async def waifu_marino(self, ctx):
        id, image = apicall.waifuapi_sfw_tag("marin-kitagawa")
        await ctx.send(f"{image}\nID = {id}")

    # MORI CALLIOPE
    @commands.command()
    async def waifu_mori_calliope(self, ctx):
        id, image = apicall.waifuapi_sfw_tag("mori-calliope")
        await ctx.send(f"{image}\nID = {id}")

    # RAIDEN SHOGUN
    @commands.command()
    async def waifu_raiden_shogun(self, ctx):
        id, image = apicall.waifuapi_sfw_tag("raiden-shogun")
        await ctx.send(f"{image}\nID = {id}")

    # SELFIES
    @commands.command()
    async def waifu_selfies(self, ctx):
        id, image = apicall.waifuapi_sfw_tag("selfies")
        await ctx.send(f"{image}\nID = {id}")

    # UNIFORM
    @commands.command()
    async def waifu_uniform(self, ctx):
        id, image = apicall.waifuapi_sfw_tag("uniform")
        await ctx.send(f"{image}\nID = {id}")

    # GENSHIN IMPACT
    @commands.command()
    async def waifu_genshin(self, ctx):
        id, image = apicall.waifuapi_sfw_tag("genshin-impact")
        await ctx.send(f"{image}\nID = {id}")


async def setup(bot):
    await bot.add_cog(Sfw(bot))
