from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, Body, Request, Form,UploadFile,File
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from bson.objectid import ObjectId
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import os
import datetime

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

#================== ASK and ANSWER by MODEL ========================

@app.get('/ask')
async def testfunction(request: Request):
    question = content= ""
    return templates.TemplateResponse("askV2.html",{"request": request,"content":content,"question":question ,"predictAns":""  })

@app.post('/ask')
async def testfunction(request: Request, question: str  = Form(...), content: str  = Form(...)):
    # predictAns = findAnswer(question,content)[0]['answer']
    predictAns = ""
    if(not predictAns):
        predictAns = "No Answer"
    return templates.TemplateResponse("askV2.html",{"request": request,"content":content,"question":question ,"predictAns": predictAns })


#================== ASK and ANSWER by MODEL ========================


@app.post('/voice2text')
async def receiveData(request: Request,file: UploadFile= File(...)):

    audio_bytes = file.file.read()
    
    with open("audio.wav","wb") as f: 
        f.write(audio_bytes)
    
    #call voice2text to convert voice recorded to text
    # question = Voice2Text("audio.wav")
    #call answeringQA model and ggapi to search answer
    # predictAns = findAnswer(question,content)[0]['answer']
    
    content= "Nội dung người dùng nhập"
    
    question = "kết quả trả từ model voice to text"
    
    predictAns = "kết quả từ model đọc hiểu văn bản"
    return RedirectResponse(templates.TemplateResponse("askV2.html",{"request": request,"content":content,"question":question ,"predictAns": predictAns}))
    
@app.get('/voice2text')
async def receiveData():
    return "kết quả trả từ model voice to text"
