"""
Example: Searching for Videos

If you want use additinal arguments below
    
search_videos() additional arguments:
orientation (string - optional):    Desired photo or video orientation. 
                                    The current supported orientations are: "landscape", "portrait" or "square".

size (string - optional):           Minimum photo or video size. 
                                    The current supported sizes are: large (24MP), medium (12MP) or small (4MP).

locale (string - optional):         The locale of the search you are performing. 
The current supported locales are:  "en-US", "pt-BR", "es-ES", "ca-ES", "de-DE", "it-IT", "fr-FR", "sv-SE", "id-ID", "pl-PL", 
                                    "ja-JP", "zh-TW", "zh-CN", "ko-KR", "th-TH", "nl-NL", "hu-HU", "vi-VN", "cs-CZ", "da-DK", 
                                    "fi-FI", "uk-UA", "el-GR", "ro-RO", "nb-NO", "sk-SK", "tr-TR", 'ru-RU".
"""

import asyncio
from pexels_async_api.client import AsyncPexelsClient

async def main():
    client = AsyncPexelsClient("your_api_key")  # replace "your_api_key" with your actual Pexels API key
    videos = await client.search_videos("cats", per_page=5, page=1)
    print(videos)

# Run the main function
asyncio.run(main())
