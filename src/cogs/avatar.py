import discord
from discord.ext import commands


class avatar_command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="avatar",
        usage="!avatar o !avatar @user",
        description=" Muestra el avatar de una persona"
    )
    async def avatar(self, ctx, member: discord.Member = None):
        if member is None:
            embed = discord.Embed(
                title=" El comando usado deberia ser **!avatar [miembro]**",
                color = discord.color.red(),
                footer=ctx.message.created_at
            )
            await ctx.send(embed=embed)
        else:
            embed2 = discord.Embed(
                title=f"!Avatar de {member} (ufff y estas guapo)",
                color = 0x486F8C,
                timestamp=ctx.message.created_at
            )
            embed2.add_field(
                name="Pero estas Animado?",
                value=member.is_avatar_animated())
            embed2.set_image(url=member.avatar_url)
            await ctx.send(embed=embed2)


def setup(bot):
    bot.add_cog(avatar_command(bot))
