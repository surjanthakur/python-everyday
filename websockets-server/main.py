from fastapi import FastAPI, WebSocket, WebSocketDisconnect, WebSocketException
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    </head>
    <body>
        <h1>WebSocket Chat</h1>

        <h2 class="text-danger">you id: <span id="ws-id"></span></h2>
   
        <form action="" class="mt-5" onsubmit="sendMessage(event)">
            <input type="text" class="form control" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>

        <ul id='messages' class="mt-5>
        </ul>

      <script>
      let client_id = Date.now()
      document.querySelector('#ws-id').textContent = client_id
      let ws = new WebSocket("ws://localhost:8000/ws/connection/${client_id}");
            ws.onmessage = function(event) {
                let messages = document.getElementById('messages');
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


@app.websocket("/ws/connection/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    try:
        await socket_manager.connect_connection(websocket)
        while True:
            data = websocket.receive_text()
            await socket_manager.send_messages(f"you wrote: {data}", websocket)
            await socket_manager.brodcast_messages(f"client {client_id} says: {data}")
    except WebSocketDisconnect:
        socket_manager.close_connection(websocket)
        await socket_manager.brodcast_messages(f"client {client_id} has left the chat")
        print("connection close")


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="localhost", port=8000)
