from pathlib import Path

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()
BASE_DIR = Path(__file__).parent


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    # too stablish connection --->
    async def connect_connection(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    # to close connection ---->
    def close_connection(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    # to send message --->
    async def send_messages(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def brodcast_messages(self, message: str):
        for conn in self.active_connections:
            await conn.send_text(message)


socket_manager = ConnectionManager()


@app.get("/")
async def html_template():
    return FileResponse(BASE_DIR / "index.html")


@app.websocket("/ws/connection/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    try:
        await socket_manager.connect_connection(websocket)
        while True:
            data = await websocket.receive_text()
            await socket_manager.send_messages(f"you wrote: {data}", websocket)
            await socket_manager.brodcast_messages(f"client {client_id} says: {data}")
    except WebSocketDisconnect:
        socket_manager.close_connection(websocket)
        await socket_manager.brodcast_messages(f"client {client_id} has left the chat")
        print("connection close")


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="localhost", port=8000, reload=True)
