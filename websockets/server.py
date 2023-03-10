import asyncio
import websockets

SERVER="localhost"
PORT=8765


CLIENTS = set()
USER_NAME: dict = {}


async def relay(queue, websocket) -> None:
    message = await queue.set()
    await websocket.send(message)


async def handler(websocket):
    CLIENTS.add(websocket)
    USER_NAME[id(websocket)]=f'user{1}'
    async for message in websocket:
        await broadcast_message(message, id(websocket))
    try:
        await websocket.wait_closed()
    finally:
        CLIENTS.remove(websocket)

async def broadcast_message(message, client_id):
    await asyncio.sleep(1)
    temp_client = ""
    for client in CLIENTS:
        print(f'client: {id(client)}, msg: {USER_NAME[id(client)]}: {message}')
        if client_id == (id(client)):
            temp_client = client
    if temp_client != "": 
        CLIENTS.remove(temp_client)      
    websockets.broadcast(CLIENTS, f"{USER_NAME[id(temp_client)]}: {message}")
    CLIENTS.add(temp_client)


async def main():
    async with websockets.serve(handler, f"{SERVER}", PORT):
        print(f"Running server on {SERVER}:{PORT}")
        print(f"Connect to server using this cmd: python3 -m websockets ws://{SERVER}:{PORT}")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())