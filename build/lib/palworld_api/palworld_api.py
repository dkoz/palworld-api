import aiohttp
import asyncio

class PalworldAPI:
    def __init__(self, server_url, username, password):
        """
        Initializes the API wrapper instance.
        """
        self.server_url = server_url
        self.auth = aiohttp.BasicAuth(login=username, password=password)
        self.headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    async def fetch(self, session, url):
        """
        General method for fetching data from a given URL.
        """
        try:
            async with session.get(url, headers=self.headers, auth=self.auth) as response:
                response.raise_for_status()
                if 'application/json' in response.headers.get('Content-Type', ''):
                    return await response.json()
                else:
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
        async with aiohttp.ClientSession() as session:
            url = f"{self.server_url}/v1/api/info"
            return await self.fetch(session, url)

    async def get_player_list(self):
        """
        Retrieves the list of players.
        """
        async with aiohttp.ClientSession() as session:
            url = f"{self.server_url}/v1/api/players"
            return await self.fetch(session, url)

    async def get_server_metrics(self):
        """
        Retrieves server metrics.
        """
        async with aiohttp.ClientSession() as session:
            url = f"{self.server_url}/v1/api/metrics"
            return await self.fetch(session, url)
    
    async def get_server_settings(self):
        """
        Retrieves server settings.
        """
        async with aiohttp.ClientSession() as session:
            url = f"{self.server_url}/v1/api/settings"
            return await self.fetch(session, url)

    async def kick_player(self, userid, message):
        """
        Kicks a player from the server.
        """
        url = f"{self.server_url}/v1/api/kick"
        payload = {"userid": userid, "message": message}
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, headers={'Content-Type': 'application/json'}, auth=self.auth) as response:
                response.raise_for_status()
                try:
                    return await response.json()
                except aiohttp.ContentTypeError:
                    return await response.text()

    async def ban_player(self, userid, message):
        """
        Bans a player from the server.
        """
        url = f"{self.server_url}/v1/api/ban"
        payload = {"userid": userid, "message": message}
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, headers={'Content-Type': 'application/json'}, auth=self.auth) as response:
                response.raise_for_status()
                try:
                    return await response.json()
                except aiohttp.ContentTypeError:
                    return await response.text()
                
    async def unban_player(self, userid):
        """
        Unbans a player from the server.
        """
        url = f"{self.server_url}/v1/api/unban"
        payload = {"userid": userid}
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, headers={'Content-Type': 'application/json'}, auth=self.auth) as response:
                response.raise_for_status()
                try:
                    return await response.json()
                except aiohttp.ContentTypeError:
                    return await response.text()
                
    async def save_server_state(self):
        """
        Saves the current state of the server.
        """
        url = f"{self.server_url}/v1/api/save"
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=self.headers, auth=self.auth) as response:
                response.raise_for_status()
                try:
                    return await response.json()
                except aiohttp.ContentTypeError:
                    return await response.text()
                
    async def make_announcement(self, message):
        """
        Makes an announcement to all players on the server.
        """
        url = f"{self.server_url}/v1/api/announce"
        payload = {"message": message}
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, headers=self.headers, auth=self.auth) as response:
                response.raise_for_status()
                try:
                    return await response.json()
                except aiohttp.ContentTypeError:
                    return await response.text()
    
    async def shutdown_server(self, waittime, message):
        """
        Initiates a server shutdown with a delay and displays a message to users.
        """
        url = f"{self.server_url}/v1/api/shutdown"
        payload = {"waittime": waittime, "message": message}
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, headers=self.headers, auth=self.auth) as response:
                response.raise_for_status()
                try:
                    return await response.json()
                except aiohttp.ContentTypeError:
                    return await response.text()
                
    async def stop_server(self):
        """
        Stops the server immediately.
        """
        url = f"{self.server_url}/v1/api/stop"
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=self.headers, auth=self.auth) as response:
                response.raise_for_status()
                try:
                    return await response.json()
                except aiohttp.ContentTypeError:
                    return await response.text()

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