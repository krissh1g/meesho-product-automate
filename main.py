# FastAPI backend main.pyfrom fastapi import FastAPI

app = FastAPI()  # This must exist at the top level

# Your routes here
@app.get("/")
def home():
    return {"status": "Backend running"}
from fastapi import FastAPI  # THIS IS REQUIRED

app = FastAPI()  # Must be exactly 'app'

@app.get("/")
def home():
    return {"status": "Backend running"}

