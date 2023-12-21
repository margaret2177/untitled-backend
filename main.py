# import uvicorn

# if __name__ == "__main__":
#   uvicorn.run("server.api:app", host="0.0.0.0", port=10000)

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from scraper import Scraper


# import starlette.responses as responses

s = Scraper()
origins = [
    # "http://localhost.tiangolo.com",
    # "https://localhost.tiangolo.com",
    "http://localhost:3000",
    "http://localhost:8080"


]





app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return 'Hello there!'


@app.get("/api/home/{page}")
def read_home(page:int=1):
    
    
    return s.homeThumbnail(page)


@app.get("/api/details/{path}")
def read_details(path:str):
    
    return s.itemDetails(path)


@app.get("/api/search/{term}")
def read_search(term:str,page:int=1):
 
    return s.searchResult(term,page)


# uvicorn main:app --reload

# s.homeThumbnail()
# s.itemDetails('/videos/being-a-hero-2022-episode-8')