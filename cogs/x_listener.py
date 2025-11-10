from discord.ext import commands
import discord
import re
from utils.parse import parseX_url, fetch_x_data


class XListener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
       
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.guild is None:
            return
            
        match = re.search(
            r'(?:https?://)?(?:www\.)?(?:twitter|x)\.com/\w+/status/\d+',
            message.content
        )
        if not match:
            return
        
        url = match.group(0)
        data = parseX_url(url)
        if not data:
            return
        
        tweet_data = await fetch_x_data(data['tweet_id'])
        if not tweet_data:
            return 
        
        user_info = tweet_data.get('user', {})
        nickname = user_info.get('name', data['username'])
        username = user_info.get('screen_name', data['username'])
        text = tweet_data.get('text', '')
        video_url = tweet_data.get('video_url')
        
        embed = discord.Embed(
            title=f"{nickname} (@{username})",
            description=text,
            color=0x1DA1F2,
            url=url
        )
        
        if video_url:
            embed.set_video(url=video_url)
        
        await message.channel.send(embed=embed)



async def setup(bot):
    await bot.add_cog(XListener(bot))
