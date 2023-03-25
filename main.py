# Import libraries and user defined functions
from reddit_api_handler import get_post
from fastapi import FastAPI, Request

# Build API Interface using FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/subreddit/{item_id}")
async def get_request(item_id):
    return get_post(item_id)

@app.post("/subreddit/")
async def get_body(request: Request):
    return await request.json()

