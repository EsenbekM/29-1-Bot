import time
import asyncio


async def download_photo(photo_amount, limit):
    while photo_amount < limit:
        await asyncio.sleep(1)
        photo_amount += 1
        print(f"Photo {photo_amount}")


async def download_video(video_amount, limit):
    while video_amount < limit:
        await asyncio.sleep(5)
        video_amount += 1
        print(f"video {video_amount}")
        
        
async def main():
    task_list = [download_photo(0, 20), download_video(0, 4)]
    await asyncio.gather(*task_list)

asyncio.run(main())

#  *[1, 2, 3] == 1, 2, 3
