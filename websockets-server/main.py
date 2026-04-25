from fastapi import FastAPI, WebSocket, WebSocketDisconnect, WebSocketException
from fastapi.responses import HTMLResponse

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
        # add websocket logic here
        </script>
    </body>
</html>
"""


@app.get("/")
async def html_template():
    return HTMLResponse(content=html, status_code=200)


@app.websocket("/ws/connection")
async def websocket_connection(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = websocket.receive_text()
        await websocket.send_text(f"message text was: {data}")
