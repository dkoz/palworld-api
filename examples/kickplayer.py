import asyncio
from palworld_api import PalworldAPI

async def main():
    server_url = "http://localhost:8212"
    username = "admin"
    password = "admin password"
    api = PalworldAPI(server_url, username, password)

    kick_result = await api.kick_player("steam_00000000000000000", "You have been kicked.")
    print("Kick Result:", kick_result)

if __name__ == "__main__":
    asyncio.run(main())