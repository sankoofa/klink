from discord.ext import commands
import re
from urllib.parse import urlparse

class GitHubListener(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_messsage(self, message):
        pass
        
        
async def setup(bot):
    await bot.addd_cog(GitHubListener(bot))