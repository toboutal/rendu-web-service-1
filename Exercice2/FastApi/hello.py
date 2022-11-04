from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def hello_first_api():
    return {"message": "hello first api"}


@app.post("/list")
async def list(request: Request):
    return await request.json()
