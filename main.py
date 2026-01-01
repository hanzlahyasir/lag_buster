from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from get_ping import get_ping_value
import asyncio
import logging
import json

logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

@app.websocket("/ws/ping")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    logging.info("WebSocket connected")
    try:
        while True:
            ping_value = get_ping_value()
            if ping_value is not None:
                message = json.dumps({"ping": ping_value})
                await websocket.send_text(message)
                logging.debug(f"Sent ping value: {ping_value}")
            else:
                logging.warning("Ping value not found.")
            await asyncio.sleep(2)
    except WebSocketDisconnect:
        logging.info("WebSocket disconnected")
    except Exception as e:
        logging.error(f"Error in WebSocket connection: {e}")