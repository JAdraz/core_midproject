from fastapi import FastAPI
from router import endpoints, germany_covid

app = FastAPI()

app.include_router(endpoints.router)
app.include_router(germany_covid.router)

@app.get("/")
def test():
    return {
        "API Status" : "Working"
    }