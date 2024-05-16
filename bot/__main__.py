from . import bot, owner_id

async def main():
    await bot.start()
    await bot.send_message(user_id=owner_id, message=f'<b>Instagram Downloader Bot Started!</b> @{(await bot.get_me()).user_name}')
    await bot.idle()
    await bot.stop()

bot._loop.run_until_complete(main())