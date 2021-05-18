#
#
from starlette.middleware import Middleware
from fastapi import FastAPI
#from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware

import nest_asyncio
from pyngrok import ngrok
import uvicorn

middleware = [
    Middleware(CORSMiddleware, allow_origins=["*"])
]

app = FastAPI(middleware=middleware)

class Makan:
    def simple(self):
        return "Mantap banget"

makan = Makan()

@app.get('/index')
async def home():
    kal = makan.simple()
    return {"message": makan.simple()}


@app.get('/mantap')
async def mantap():
    return {"message": "Hello World"}

@app.get('/hallo')
async def hallo():
    return {"message": "Hello World"}


# ngrok tunnel cuma buat akses pake tunnel ngrok 
# ngrok_tunnel = ngrok.connect(8000)
# print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8899, host='0.0.0.0', log_level="info")
