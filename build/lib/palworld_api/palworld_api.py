import aiohttp
import asyncio

class PalworldAPI:
    """
    API wrapper for interacting with a Palworld server.
    """
    def __init__(self, server_url, username, password):
        self.server_url = server_url
        self.auth = aiohttp.BasicAuth(login=username, password=password)
        self.headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    async def fetch(self, url):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=self.headers, auth=self.auth) as response:
                    response.raise_for_status()
                    if 'application/json' in response.headers.get('Content-Type', ''):
                        return await response.json()
                    return await response.text()
        except aiohttp.ClientResponseError as e:
            return {'error': f'Client error {e.status}: {e.message}'}
        except aiohttp.ClientConnectionError:
            return {'error': 'Connection error'}
        except asyncio.TimeoutError:
            return {'error': 'Request timeout'}
        except Exception as e:
            return {'error': str(e)}

    async def post(self, endpoint, payload=None):
        url = f"{self.server_url}{endpoint}"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=payload, headers=self.headers, auth=self.auth) as response:
                    response.raise_for_status()
                    try:
                        return await response.json()
                    except aiohttp.ContentTypeError:
                        return await response.text()
        except aiohttp.ClientResponseError as e:
            return {'error': f'Client error {e.status}: {e.message}'}
        except aiohttp.ClientConnectionError:
            return {'error': 'Connection error'}
        except asyncio.TimeoutError:
            return {'error': 'Request timeout'}
        except Exception as e:
            return {'error': str(e)}

    async def get_server_info(self):
        """
        Retrieves server information.
        """
        return await self.fetch(f"{self.server_url}/v1/api/info")

    async def get_player_list(self):
        """
        Retrieves the list of players.
        """
        return await self.fetch(f"{self.server_url}/v1/api/players")

    async def get_server_metrics(self):
        """
        Retrieves server metrics.
        """
        return await self.fetch(f"{self.server_url}/v1/api/metrics")

    async def get_server_settings(self):
        """
        Retrieves server settings.
        """
        return await self.fetch(f"{self.server_url}/v1/api/settings")

    async def kick_player(self, userid, message):
        """
        Kicks a player from the server.
        """
        return await self.post("/v1/api/kick", {"userid": userid, "message": message})

    async def ban_player(self, userid, message):
        """
        Bans a player from the server.
        """
        return await self.post("/v1/api/ban", {"userid": userid, "message": message})

    async def unban_player(self, userid):
        """
        Unbans a player from the server.
        """
        return await self.post("/v1/api/unban", {"userid": userid})

    async def save_server_state(self):
        """
        Saves the current state of the server.
        """
        return await self.post("/v1/api/save")

    async def make_announcement(self, message):
        """
        Makes an announcement to all players on the server.
        """
        return await self.post("/v1/api/announce", {"message": message})

    async def shutdown_server(self, waittime, message):
        """
        Initiates a server shutdown with a delay and displays a message to users.
        """
        return await self.post("/v1/api/shutdown", {"waittime": waittime, "message": message})

    async def stop_server(self):
        """
        Stops the server immediately.
        """
        return await self.post("/v1/api/stop")

async def main():
    server_url = "http://localhost:8212"
    username = "admin"
    password = "admin password"
    api = PalworldAPI(server_url, username, password)
    server_info = await api.get_server_info()
    print("Server Info:", server_info)
    player_list = await api.get_player_list()
    print("Player List:", player_list)
    server_metrics = await api.get_server_metrics()
    print("Server Metrics:", server_metrics)

if __name__ == "__main__":
    asyncio.run(main())
