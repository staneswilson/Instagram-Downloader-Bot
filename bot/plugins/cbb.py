from swibots import CallbackQueryEvent, BotContext
from swibots import InlineMarkup, InlineKeyboardButton

from .helper_func import is_joined
from .. import bot, community_url

@bot.on_callback_query()
async def callback(ctx: BotContext[CallbackQueryEvent]):
    query = ctx.event
    data = query.callback_data
    if data == "refresh":
        joined = await is_joined(query.user)
        if joined:
            text = f"Hello @{query.user.username}! I am a bot that can download Instagram media. Send me an Instagram URL to get started."
            markup = InlineMarkup([[
                InlineKeyboardButton("🌐Community🌐", url=community_url)
            ]])
        else:
            text = f"Hello @{query.user.username}! You need to join the community to use this bot."
            markup = InlineMarkup([
            [
                InlineKeyboardButton("🌐Join Community🌐", url=community_url)
            ],
            [
                InlineKeyboardButton("🔁Try Again🔁", callback_data="refresh")
            ]])
        
        await query.message.respond(text, inline_markup=markup)
        await query.message.delete()