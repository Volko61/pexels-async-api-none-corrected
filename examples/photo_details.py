"""
Example: Getting Details of a Specific Photo
"""

import asyncio
from pexels_async_api.client import AsyncPexelsClient

async def main():
    client = AsyncPexelsClient("your_api_key")  # replace "your_api_key" with your actual Pexels API key
    photo = await client.get_photo(123456)  # replace 123456 with the actual photo ID
    print(photo)

# Run the main function
asyncio.run(main())
