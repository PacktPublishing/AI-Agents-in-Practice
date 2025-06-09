import aiofiles
import asyncio

async def read_file():
    async with aiofiles.open("report.txt", "r") as file:
        content = await file.read()
    print("File content loaded.")

asyncio.run(read_file())
