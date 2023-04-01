# Import libraries and user defined functions
from reddit_api_handler import get_post, show_post_lists
from fastapi import FastAPI, Request, Body
from fastapi.middleware.cors import CORSMiddleware

# To run server
# uvicorn main:app --reload

# Build API Interface using FastAPI
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
    return get_post(item_id)

@app.post("/subreddit/", status_code=201)
async def show_posts(count: int = Body(...), subreddit: str = Body(...), type: str = Body(...)):
    return show_post_lists(count, subreddit, type)


