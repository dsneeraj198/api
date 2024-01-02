# main.py

from fastapi import FastAPI
from app.routers import sum,transforminput
import uvicorn

app = FastAPI()

app.include_router(sum.router)
app.include_router(transforminput.router)

if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8501)