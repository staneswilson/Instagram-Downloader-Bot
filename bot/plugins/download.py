import os
from swibots import BotContext, MessageEvent
from swibots import InlineMarkup, InlineKeyboardButton

from .instagram import download_media
from .helper_func import is_joined, rename_file
from .. import bot, LOGGER, community_url

@bot.on_message()
async def download(ctx: BotContext[MessageEvent]):
    message = ctx.event.message
    text = message.message
    user = ctx.event.user
    joined = await is_joined(user)
    
    if not joined:
        reply_text = f"Hello @{user.username}! You need to join the community to use this bot."
        reply_markup = InlineMarkup([
        [
            InlineKeyboardButton("🌐Join Community🌐", url=community_url)
        ],
        [
            InlineKeyboardButton("🔁Try Again🔁", callback_data="refresh")
        ]])
        
        await message.reply_text(reply_text, inline_markup=reply_markup)
        return
    
    if "instagram.com/" not in text:
        await message.reply_text("Enter the URL to the post, reel, story or highlight and I'll download it for you.\ne.g. https://www.instagram.com/p/abcd2egj/")
        return
    
    try:
        reply = await message.reply_text("Downloading media...")
        path = await download_media(text)

        if not path:
            raise FileNotFoundError("No file found at the provided path.")

        await reply.edit_text("Media downloaded successfully. Uploading...")

        path_n = await rename_file(path)
        LOGGER.info(f"Renamed file path: {path_n}")

        await message.reply_media(document=path_n, blocking=True)
        await reply.delete()

        os.remove(path_n)
    except FileNotFoundError as e:
        await reply.edit_text("Failed to download media. Please ensure the URL is correct and the media is publicly accessible.")
        LOGGER.error(f"FileNotFoundError: {e}")
    except Exception as e:
        await reply.edit_text("An error occurred while processing the media.")
        LOGGER.error(f"Unexpected error in download.py: {e}")