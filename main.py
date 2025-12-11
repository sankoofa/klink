import asyncio
import os
import discord
from discord.ext import commands
from config import token

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
COGS_DIR = os.path.join(BASE_DIR, "cogs")

intents = discord.Intents.default()
intents.message_content = True

class BotClient(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="k.",
            intents=intents,
            help_command=None
        )

    async def setup_hook(self):
        await self.load_all_cogs()
        await self.tree.sync()
        print("[CMD] Slash sync ✓")

    async def load_all_cogs(self):
        if not os.path.isdir(COGS_DIR):
            print("[COG] Directory not found")
            return

        for filename in sorted(os.listdir(COGS_DIR)):
            if filename.endswith(".py"):
                name = filename[:-3]
                try:
                    await self.load_extension(f"cogs.{name}")
                    print(f"[COG] {name} ✓")
                except Exception as e:
                    print(f"[COG] {name} ✗ {e}")

    async def on_ready(self):
        print(f"[BOT] {self.user} online")

async def main():
    async with BotClient() as bot:
        await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())
