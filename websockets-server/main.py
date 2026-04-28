from fastapi import FastAPI, WebSocket, WebSocketDisconnect
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

        <h2 class="text-danger">your id: <span class="text-danger" id="ws-id"></span></h2>
   
        <form action="" class="mt-5" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>

        <ul id="messages" class="mt-5">
        </ul>

      <script>
              const client_id = Date.now();
              window.addEventListener('DOMContentLoaded', () => {
                document.getElementById('ws-id').textContent = client_id;
              });
         
         
               let ws = new WebSocket(`ws://localhost:8000/ws/${client_id}`);
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


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="localhost", port=8000, reload=True)
