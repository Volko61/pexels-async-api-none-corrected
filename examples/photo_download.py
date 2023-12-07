"""
Example: Downloading a Specific Photo
"""

import asyncio
from pexels_async_api.client import AsyncPexelsClient

async def main():
    client = AsyncPexelsClient("your_api_key")  # replace "your_api_key" with your actual Pexels API key
    photo_data = await client.download_photo(123456)  # replace 123456 with the actual photo ID
    with open("photo.jpg", "wb") as f:
        f.write(photo_data)

# Run the main function
asyncio.run(main())
