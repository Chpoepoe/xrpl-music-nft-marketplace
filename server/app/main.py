from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "XRPL Music NFT API is running!"}

