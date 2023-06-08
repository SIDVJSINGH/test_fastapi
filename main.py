from fastapi import FastAPI
import uvicorn  # for ASGi
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: int
    brand: Optional[str] = None


inventory = {
    1: {
        "name": "Siddhant",
        "post": "Developer",
        "pay": 500
    },
    2: {
        "name": "Lawerence",
        "post": "teacher",
        "pay": 100
    }
}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/all")
async def all_data():
    return inventory


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/opti/{param}/{id}")
async def param_get(*, param: Optional[str] = None, integer: int):
    return {"data": f"{param} and {integer}"}


# Query Parameters
@app.get("/para")
async def para(*, name: Optional[str] = None, pay: Optional[int]):
    for item_id in inventory:
        if inventory[item_id]['name'] == name or inventory[item_id]['pay'] == pay:
            return inventory[item_id]
    return {"Data": "Not Found"}


@app.get("/para/{item}")
async def para(*, item_i: int = None, name: Optional[str] = None, pay: Optional[int] = None):
    for i in range(len(inventory)):
        if item_i == i:
            if inventory[i]['name'] == name or inventory[i]['pay'] == pay:
                return inventory[i]
            else:
                return inventory[i]

    return {"Data": "Not Found"}


@app.post("/create-item/{item_id}")
async def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item_id Already Exists"}
    inventory[item_id] = dict(name=item.name, brand=item.brand, price=item.price)
    return inventory[item_id]


# Running the api with uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)

print(len(inventory))
