"""
Example: Getting Curated Photos
"""

import asyncio
from pexels_async_api.client import AsyncPexelsClient

async def main():
    client = AsyncPexelsClient("your_api_key")  # replace "your_api_key" with your actual Pexels API key
    curated_photos = await client.get_curated_photos(per_page=5, page=1)
    print(curated_photos)

# Run the main function
asyncio.run(main())
