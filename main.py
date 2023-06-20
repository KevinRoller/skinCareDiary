from Predictor import predictor
from typing_extensions import Annotated

from fastapi import FastAPI, File, UploadFile
from fastapi.logger import logger
from pydantic import BaseSettings
import os
import sys
import io
from PIL import Image
from fastapi.responses import FileResponse
import cv2
import datetime

predictor_api=predictor()
file_path="./stored_image/"

# class Settings(BaseSettings):
#     # ... The rest of our FastAPI settings
#     BASE_URL = "http://localhost:8000"
#     USE_NGROK = os.environ.get("USE_NGROK", "False") == "True"
# settings = Settings()

# def init_webhooks(base_url):
#     # Update inbound traffic via APIs to use the public-facing ngrok URL
#     pass

app = FastAPI()

# if settings.USE_NGROK:
# pyngrok should only ever be installed or initialized in a dev environment when this flag is set
# from pyngrok import ngrok

# Get the dev server port (defaults to 8000 for Uvicorn, can be overridden with `--port`
# when starting the server
# port = sys.argv[sys.argv.index("--port") + 1] if "--port" in sys.argv else 8000

# # Open a ngrok tunnel to the dev server
# public_url = ngrok.connect(port).public_url
# logger.info("ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(public_url, port))
# print(("ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(public_url, port)))
# # Update any base URLs or webhooks to use the public ngrok URL
# settings.BASE_URL = public_url
# init_webhooks(public_url)


# @app.post("/files/")
# async def create_file(file: Annotated[bytes, File()]):
#     return {"file_size": len(file)}

# import base64

# file_content = 'b2xhIG11bmRv'
import secrets

def generate_random_token():
    token = secrets.token_hex(16)
    return token
def getCurentDateTime():
    now=datetime.datetime.now()

    return  {
        "year": now.year,
        "month": now.month,
        "day": now.day,
        "hour": now.hour,
        "minute": now.minute,
        "second": now.second,
        "microSecond":now.microsecond
        }

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):#=File(...)):
    # print(file)
    print("dummy")
    content=await file.read()
    # print(content)
    # try:
    #     content=base64.b64decode(content)
    #     print(content)
    #     with open("./image.jpg","w+") as f:
    #         f.write(content.decode("utf-8"))
    # except Exception as e:
    #     print(str(e))
    rand_file_name=generate_random_token()+".jpg"
    pil_image=Image.open(io.BytesIO(content))
    cv2_image,ance_count=predictor_api(pil_image)
    cv2.imwrite(file_path+rand_file_name,cv2_image)
    # pil_image.save(file_path+rand_file_name)

    #return {"abc":"xyz"}
    return {"image_path":"get_result_image/"+rand_file_name,"ance_count":ance_count,**getCurentDateTime()}
# from fastapi import FastAPI
# app = FastAPI()

@app.get("/get_result_image/{path}")
async def get_image(path:str):
    return FileResponse(file_path+path)

@app.get("/")
async def root():
    return {"message": "Hello World"}