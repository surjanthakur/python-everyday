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


@app.get("/")
async def html_template():
    return HTMLResponse(content=html, status_code=200)


@app.websocket("/ws/connection")
async def websocket_connection(websocket: WebSocket):
    try:
        await websocket.accept()

        while True:
            data = await websocket.receive_text()
            if "quit" in data or "close" in data:
                await websocket.send_text("Closing connection")
                await websocket.close(
                    code=1000, reason="client req to close the connection"
                )
                break
            await websocket.send_text(f"message text was: {data}")
    except WebSocketDisconnect:
        print("Client disconnected")


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="localhost", port=8000)
