import os
import logging
from fastapi import FastAPI

logging.basicConfig(level=logging.INFO)
app = FastAPI(title="Hello K3s", docs_url="/docs")

VERSION = os.getenv("APP_VERSION", "dev")


@app.get("/")
def root():
    return {"message": "Hello from FastAPI on k3s!", "version": VERSION}


@app.get("/healthz")
def healthz():
    return {"status": "ok"}
