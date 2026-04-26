from fastapi import FastAPI, WebSocket, WebSocketDisconnect, WebSocketException
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
      <script>
            let ws = new WebSocket("ws://localhost:8000/ws/connection");
            ws.onmessage = function(event) {
                let messages = document.getElementById('messages')
                let message = document.createElement('li')
                let content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                let input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


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
    return HTMLResponse(content=html, status_code=200)


@app.websocket("/ws/connection")
async def websocket_endpoint(websocket: WebSocket):
    pass


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="localhost", port=8000)
