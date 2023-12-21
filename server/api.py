from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from server.routes import router as Router



# import starlette.responses as responses


origins = [
    # "http://localhost.tiangolo.com",
    # "https://localhost.tiangolo.com",
    "https://asianembed.io",
    "https://floating-spire-08257.herokuapp.com",
    "http://localhost:3000"

]





app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(Router)
# s=Scraper()

# @app.get("/")
# async def read_root():
#     return 'Hello there!'


# @app.get("/api/home/")
# async def read_home(page:int=1,filter:str='RAS'):
    
   

#     return s.homeThumbnail(page,filter)

# @app.get("/api/details/{path}")
# async def read_details(path:str):
    
#     return s.itemDetails(path)

# @app.get("/api/search/{term}")
# async def read_search(term:str,page:int=1):
 
#     return s.searchResult(term,page)


# uvicorn main:app --reload

# s.homeThumbnail()
# s.itemDetails('/videos/being-a-hero-2022-episode-8')