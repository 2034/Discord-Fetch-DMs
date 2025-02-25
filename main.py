import os
import sys
from discord.ext import commands

def getToken():
    if os.path.exists("token.txt"):
        with open("token.txt", "r") as f:
            token = f.read().strip()
            if not token:
                print("Token is required to proceed.")
                sys.exit(1)
            return token
    else:
        token = input("Enter your Discord token (will not echo): ")
        if not token:
            print("Token is required to proceed.")
            sys.exit(1)
        
        with open("token.txt", "w") as f:
            f.write(token)
        return token

async def scrapeDMS(bot, targetId):
    user = bot.get_user(targetId)
    channel = await user.create_dm()

    if not channel:
        print("You do not have DMs with this user")
        await bot.close()
        return

    if os.path.exists(f"{targetId}"):
        os.system(f"rmdir /S /Q {targetId}")
        print("Deleted old folder")

    os.mkdir(f"{targetId}")
    os.mkdir(f"{targetId}/attachments")

    print("Fetching messages...")
    async for message in channel.history(limit=None):
        formatted_message = f"[{message.created_at}] {message.author}: {message.content}\n"
        with open(f"{targetId}/{targetId}.txt", "a", encoding="utf-8") as f:
            f.write(formatted_message)
        
        for attachment in message.attachments:
            await attachment.save(f"{targetId}/attachments/{attachment.filename}")

    print("Scraping Done")
    await bot.close()

def main():
    TOKEN = getToken()
    bot = commands.Bot(command_prefix="!", self_bot=True)

    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user}")
        targetId = int(input("Enter the user's Discord ID you want to scrape: "))
        await scrapeDMS(bot, targetId)

    try:
        bot.run(TOKEN)
    except Exception as e:
        print(f"Error running bot: {e}")

if __name__ == "__main__":
    main()