from instagrapi.types import Media

from .. import LOGGER, insta, downloads

async def download_media(url):
    try:
        if "stories" in url:
            media_pk = insta.story_pk_from_url(url)
            file = insta.story_download(story_pk=media_pk, folder=downloads)
        else:
            media_pk = insta.media_pk_from_url(url)
            minfo = insta.media_info(media_pk)

            download_functions = {
                1: insta.photo_download,
                2: {
                    "feed": insta.video_download,
                    "igtv": insta.igtv_download,
                    "clips": insta.clip_download
                },
                8: insta.album_download
            }

            download_function = download_functions.get(minfo.media_type)

            if isinstance(download_function, dict):
                download_function = download_function.get(minfo.product_type)

            if download_function:
                if minfo.product_type == 8:
                    file = download_function(media_pk, downloads, minfo)
                else:
                    file = list(download_function(media_pk, downloads))
            else:
                LOGGER.info(f"Media type not supported: {minfo.media_type}")
                raise Exception

        return file

    except Exception as e:
        LOGGER.warning(f"Failed to download {url}: {e}")