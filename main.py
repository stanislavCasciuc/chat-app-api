from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.websockets import WebSocket, WebSocketDisconnect
from discussion.discussion import discussion_router
from messages.messages import messages_router
from sockets.manager import ConnectionManager
from users.users import login_router
from users.register import register_router
from contacts.contacts import contacts_router
app=FastAPI()

app.include_router(register_router)
app.include_router(login_router)
app.include_router(contacts_router)
app.include_router(discussion_router)
app.include_router(messages_router)

manager=ConnectionManager()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # You can restrict this to specific HTTP methods (e.g., ["GET", "POST"])
    allow_headers=["*"],  # You can restrict this to specific headers if needed
)

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket)

    try:
        while True:
            message = await websocket.receive_text()
            await manager.broadcast(message)
    except WebSocketDisconnect:
        manager.disconnect(websocket)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)