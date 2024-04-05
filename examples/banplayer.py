import asyncio
from palworld_api import PalworldAPI

async def main():
    server_url = "http://localhost:8212"
    username = "admin"
    password = "admin password"
    api = PalworldAPI(server_url, username, password)

    ban_result = await api.ban_player("steam_00000000000000000", "You have been banned.")
    print("Ban Result:", ban_result)

if __name__ == "__main__":
    asyncio.run(main())