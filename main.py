# Import libraries and user defined functions
from reddit_api_handler import get_posts
from fastapi import FastAPI, Request, Body
from fastapi.middleware.cors import CORSMiddleware
from scrapper import list_popular
import uvicorn

# To run server
# uvicorn main:app --reload

# Build API Interface using FastAPI
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8080)

app = FastAPI()

origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/subreddit/{item_id}")
async def get_request(item_id):
    return get_posts(item_id)

@app.post("/subreddit/", status_code=201)
async def show_posts(post_limit: int = Body(...), subreddit: str = Body(...), type: str = Body(...)):
    return get_posts(subreddit, type, post_limit)

@app.get("/popular/{type}", status_code=201)
async def show_popular(type):
    scrap_url = 'https://www.reddit.com/r/popular/'
    scrap_url = scrap_url + type
    return list_popular(scrap_url)

