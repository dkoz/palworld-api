# Palworld REST API Wrapper
 `palworld-api` is an API wrapper for the new Palworld Rest API. This supports all endpoints of the API and has been thoroughly tested.

## Version
> v1.0.0

## Installation
1. Install `palworld-api` using pip:
   ```bash
   pip install palworld-api
   ```

## Requirements
- Python 3.8+
- RestAPI Enabled

## Usage
 Refer to example files to get an idea of how this works. Here is a basic usage:
 ```
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