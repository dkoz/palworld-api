import asyncio
from palworld_api import PalworldAPI

async def main():
    server_url = "http://localhost:8212"
    username = "admin"
    password = "admin password"
    api = PalworldAPI(server_url, username, password)

    shutdown_result = await api.shutdown_server(30, "Server will shutdown in 30 seconds.")
    print("Shutdown Result:", shutdown_result)

if __name__ == "__main__":
    asyncio.run(main())