
import websockets
import asyncio

async def hello():
    uri="ws://localhost:15348"
    async with websockets.connect(uri) as websocket:
        recv = await websocket.recv()
        print(f"> {recv}")

async def main():
    while 1:
        await hello()

if __name__=="__main__":
    asyncio.run(main())
