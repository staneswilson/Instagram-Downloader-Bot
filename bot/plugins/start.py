from .. import bot, community_url
from .helper_func import is_joined

from swibots import BotContext, CommandEvent
from swibots import InlineMarkup, InlineKeyboardButton

@bot.on_command("start")
async def start(ctx: BotContext[CommandEvent]):
    message = ctx.event.message
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
    else:
        reply_text = f"Hello @{user.username}! I am a bot that can download Instagram media. Send me an Instagram URL to get started."
        reply_markup = InlineMarkup([[
            InlineKeyboardButton("🌐Community🌐", url=community_url)
        ]])
        
    await message.reply_text(reply_text, inline_markup=reply_markup)
    

# @bot.on_command("help")
# async def help(ctx: BotContext[CommandEvent]):
#     message = ctx.event.message
#     user = ctx.event.user
#     joined = await is_joined(user)
    
#     if not joined:
#         reply_text = f"Hello @{user.username}! You need to join the community to use this bot."
#         reply_markup = InlineMarkup([
#         [
#             InlineKeyboardButton("Join Community🌐", url=community_url)
#         ],
#         [
#             InlineKeyboardButton("🔁Try Again🔁", callback_data="refresh")
#         ]])
#     else:
#         reply_text = f"Hello @{user.username}! I am a bot that can download Instagram media. Send me an Instagram URL to get started."
#         reply_markup = InlineMarkup([[
#             InlineKeyboardButton("🌐Community🌐", url=community_url)
#         ]])
        
#     await message.reply_text(reply_text, inline_markup=reply_markup)
    
#     return