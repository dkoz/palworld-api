import asyncio
from palworld_api import PalworldAPI

async def main():
    server_url = "http://localhost:8212"
    username = "admin"
    password = "admin password"
    api = PalworldAPI(server_url, username, password)

    announcement_result = await api.make_announcement("Hello, Palworld!")
    print("Announcement Result:", announcement_result)

if __name__ == "__main__":
    asyncio.run(main())