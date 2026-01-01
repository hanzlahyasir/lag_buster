import asyncio
import websockets

async def test_websocket_ping():
    uri = "ws://localhost:8000/ws/ping"
    async with websockets.connect(uri) as websocket:
        print("Connected to WebSocket server")
        while True:
            message = await websocket.recv()
            print(f"Received message: {message}")
            await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(test_websocket_ping())