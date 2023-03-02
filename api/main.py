from fastapi import FastAPI
from router import endpoints

app = FastAPI()

app.include_router(endpoints.router)

@app.get("/")
def test():
    return {
        "API Status" : "Working"
    }