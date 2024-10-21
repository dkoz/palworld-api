# Palworld REST API Wrapper
 This is a simple Palworld REST API Wrapper for Python project. This supports all API endpoints for Palworld.

## Version
> v1.0.3

## Installation
1. Install `palworld-api` using pip:
   ```bash
   pip install palworld-api
   ```
2. Import into your project.
   ```python
   import asyncio
   from palworld_api import PalworldAPI
   ```

## Requirements
- Python 3.11+
- RestAPI Enabled

## Usage
 Refer to example files to get an idea of how this works. Here is a basic usage:
 ```python
import asyncio
from palworld_api import PalworldAPI

async def main():
    server_url = "http://localhost:8212"
    username = "admin"
    password = "admin password"
    api = PalworldAPI(server_url, username, password)

    server_info = await api.get_server_info()
    print("Server Info:", server_info)

if __name__ == "__main__":
    asyncio.run(main())
```

## Resources
 For detailed documentation on the Palworld REST API, check out the official [REST API Documentation](https://tech.palworldgame.com/api/rest-api/palwold-rest-api/).
