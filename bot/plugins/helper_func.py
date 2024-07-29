import os
from pathlib import Path
from .. import bot, community, LOGGER

async def is_joined(user):
    joined = await bot.get_community_member(community_id=community, user_id=user.id)
    if joined:
        return True

async def rename_file(file):
    img = ['webp']
    for r in img:
        if r in str(file):
            new_name = str(file).rsplit('.', 1)[0] + '.jpeg'
            os.rename(file, new_name)
            new_name = Path(new_name)
            LOGGER.info(f"Renamed file path: {str(new_name)}")

        else:
            new_name = file
    return str(new_name)