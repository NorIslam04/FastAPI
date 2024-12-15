from fastapi import FastAPI,Path

app = FastAPI()

data={
    1:{
        "name":"John",
        "age":25
    },
    2:{
        "name":"Jane", 
        "age":22
    }
}


@app.get("/")#root path
def read_root():#function to be executed when root path is accessed
    return {"message": "Hello World"}#json format response

@app.get("/data/{item_id}")#path with parameter item_id 
def read_data(item_id: int = Path(...,description="enter the ID of user!",gt=0)):#function to be executed when path is accessed
    return data[item_id]#return data with key as item_id