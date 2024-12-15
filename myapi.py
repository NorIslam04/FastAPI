from fastapi import FastAPI,Path
from typing import Optional
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

#path with parameter item_id 
#use: /data/1
@app.get("/data/{item_id}")
def read_data(item_id: int = Path(...,description="enter the ID of user!",gt=0)):#function to be executed when path is accessed
    return data[item_id]#return data with key as item_id

#path with query parameter, item_id is optional
#use: /data/?item_id=1 or /data/
@app.get("/data/")
#def get_with_name(name: Optional[str] =None,test : int): #this will give error because of test parameter is not optional we must first define non optional parameters then optional parameters
def get_with_name(test : int ,name: Optional[str]=None):
    for key in data:
        if data[key]["name"].lower()==name.lower():
            return data[key]
    return {"error":"Data not found!"}

#path with query parameter,and parameter item_id
#use: /data/1/?name=John
@app.get("/data/{item_id}/")
def read_data_with_name(item_id:int,name: Optional[str]=None):
    if data[item_id]["name"].lower()==name.lower():
        return data[item_id]
    return {"error":"Data not found!"}
