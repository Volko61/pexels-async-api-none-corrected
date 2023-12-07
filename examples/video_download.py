"""
Example: Downloading a Specific Video
"""

import asyncio
from pexels_async_api.client import AsyncPexelsClient

async def main():
    client = AsyncPexelsClient("your_api_key")  # replace "your_api_key" with your actual Pexels API key
    video_data = await client.download_video(123456)  # replace 123456 with the actual video ID
    with open("video.mp4", "wb") as f:
        f.write(video_data)

# Run the main function
asyncio.run(main())
