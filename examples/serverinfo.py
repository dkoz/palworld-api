import asyncio
from palworld_api import PalworldAPI

async def main():
    server_url = "http://localhost:8212"
    username = "admin"
    password = "admin password"
    api = PalworldAPI(server_url, username, password)

    # Retrieve server information
    server_info = await api.get_server_info()
    print("Server Info:", server_info)

    # Retrieve player list
    player_list = await api.get_player_list()
    print("Player List:", player_list)

    # Retrieve server metrics
    server_metrics = await api.get_server_metrics()
    print("Server Metrics:", server_metrics)

if __name__ == "__main__":
    asyncio.run(main())