from fastapi import FastAPI

app = FastAPI()

@app.get("/")#root path
def read_root():#function to be executed when root path is accessed
    return {"message": "Hello World"}#json format response