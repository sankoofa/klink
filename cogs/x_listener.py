from discord.ext import commands
import re
from utils import parse

class XListener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
       
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.guild is None:
            await message.channel.send('no time in dms tro')
            return
            
        match = re.search(
            r'(?:https?://)?(?:www\.)?(?:twitter|x)\.com/\w+/status/\d+',
            message.content
        )
        if not match:
            return
        
        url = match.group(0)
        
        # data = parse.parse_url(url)
        # if not data:
        #     return
        
        

async def setup(bot):
 await bot.add_cog(XListener(bot))