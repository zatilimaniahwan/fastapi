from fastapi import FastAPI
from model.TestModel import TestModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Fast API Tutorial"}

@app.get("/items/{item_id}")
async def fetch_item(item_id: TestModel):
    if(item_id == TestModel.zatil):
        return {"item_id": item_id}
    elif(item_id == TestModel.zahirah):
        return {"item_id": item_id}

    return {"message": "Not found"}

