import asyncio
from palworld_api import PalworldAPI

async def main():
    server_url = "http://localhost:8212"
    username = "admin"
    password = "admin password"
    api = PalworldAPI(server_url, username, password)

    unban_result = await api.unban_player("steam_00000000000000000")
    print("Unban Result:", unban_result)

if __name__ == "__main__":
    asyncio.run(main())