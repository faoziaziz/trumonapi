#
# export CONNECTIONSTRING=mysql://pos_almar:@Alm4r2020@localhost/trumon
from starlette.middleware import Middleware
from fastapi import FastAPI
#from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware

import nest_asyncio
from pyngrok import ngrok
import uvicorn
from pydantic import BaseModel
import datetime
import os
from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, DateTime, ForeignKey, CHAR, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



CONNECTIONSTRING = os.getenv('CONNECTIONSTRING')
engine = create_engine(CONNECTIONSTRING)

Base = declarative_base(engine)

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class Transaksi(Base):
    __tablename__ = "Transaksi"
    __table_args__ = {"autoload": True}


middleware = [
    Middleware(CORSMiddleware, allow_origins=["*"])
]

app = FastAPI(
    title="Trumon Api",
    description="Just trumon simple api",
    middleware=middleware,
)

class Makan:
    def simple(self):
        return "Mantap banget"

makan = Makan()


@app.get('/transaksi')
async def GetTrans(DevID: str = "ALMAR0000003"):

    transList = []

    transaksis = session.query(Transaksi).all()
    
    for item in transaksis:
        #contactType = session.query(ContactType).filter(ContactType.ContactTypeId == item.ContactTypeId).one()
        #emails = [item.__dict__ for item in session.query(Email).filter(Email.ContactId == item.ContactId)]
        #phoneNumbers = [item.__dict__ for item in session.query(PhoneNumber).filter(PhoneNumber.ContactId == item.ContactId)]

        trans = {
            "SeqNum": item.SeqNum,
            "DeviceId": item.DeviceId,
            "RefSN": item.RefSN,
            "FileTime": item.FileTime,
            "Nomor": item.Nomor,
            "Tanggal": item.Tanggal,
            "Jam": item.Jam,
            "Nilai": item.Nilai,
            "Pajak": item.Pajak,
            "NilaiDanPajak": item.NilaiDanPajak,
            "CustomField1": item.CustomField1,
            "CustomField2": item.CustomField2,
            "CustomField3": item.CustomField3,
            "FlagTransfer": item.FlagTransfer,
        }

        if(item.DeviceId==DevID):
            transList.append(trans)
        #print(transList)

    return {"data": transList}
    

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
