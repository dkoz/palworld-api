import asyncio
from palworld_api import PalworldAPI

async def main():
    server_url = "http://localhost:8212"
    username = "admin"
    password = "admin password"
    api = PalworldAPI(server_url, username, password)

    player_list = await api.get_player_list()
    print("Player List:", player_list)

if __name__ == "__main__":
    asyncio.run(main())