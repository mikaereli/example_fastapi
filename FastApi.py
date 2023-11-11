from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Defining entities

class User(BaseModel):
    id: int
    name: str

class Order(BaseModel):
    id: int
    product_name: str
    product_count: int
    is_cancelled: bool
    user_id: int

app = FastAPI()

# Create lists "users" and "orders" for saving entities

users: List[User] = []
orders: List[Order] = []

# HTTP-handler

@app.post("/users")
async def create_user(name: str):
    user_id = len(users) + 1
    user = User(id=user_id, name=name)
    users.append(user)
    return {"id": user_id}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return {"id": user.id, "name": user.name}
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/orders")
async def create_order(user_id: int, product_name: str, product_count: int):
    for user in users:
        if user.id == user_id:
            order_id = len(orders) + 1
            order = Order(id=order_id, product_name=product_name, product_count=product_count,
                          is_cancelled=False, user_id=user_id)
            orders.append(order)
            return {"id": order_id}
    raise HTTPException(status_code=404, detail="User not found")

@app.patch("/orders/{order_id}")
async def cancel_order(order_id: int):
    for order in orders:
        if order.id == order_id:
            order.is_cancelled = True
            return
    raise HTTPException(status_code=404, detail="Order not found")

@app.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    for order in orders:
        if order.id == order_id:
            orders.remove(order)
            return
    raise HTTPException(status_code=404, detail="Order not found")

@app.get("/orders/{order_id}")
async def get_order(order_id: int, product_name: str, is_cancelled: bool):
    total_product_count = 0
    for order in orders:
        if order.id == order_id and order.product_name == product_name and order.is_cancelled == is_cancelled:
            total_product_count += order.product_count
    return {"total_product_count": total_product_count}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
