from random import randint
import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

DATABASE_URL = "sqlite:///mydatabase.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(20)),
    sqlalchemy.Column("email", sqlalchemy.String(50)),
)

items = sqlalchemy.Table(
    "items",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(50)),
    sqlalchemy.Column("description", sqlalchemy.String(256)),
    sqlalchemy.Column("price", sqlalchemy.Float),
)

orders = sqlalchemy.Table(
    "orders",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id")),
    sqlalchemy.Column("item_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("items.id")),
    sqlalchemy.Column("order_date", sqlalchemy.DateTime),  # Добавлена дата заказа
    sqlalchemy.Column("status", sqlalchemy.String(20)),  # Добавлен статус заказа
)

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

metadata.create_all(engine)

class UserIn(BaseModel):
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)

class ItemIn(BaseModel):
    name: str = Field(max_length=128)
    description: str = Field(max_length=256)  # Добавлено описание товара
    price: float

class OrderIn(BaseModel):
    user_id: int
    item_id: int
    description: str = Field(max_length=256)  # Добавлено описание заказа

class User(BaseModel):
    id: int
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)

class Item(BaseModel):
    id: int
    name: str = Field(max_length=128)
    description: str = Field(max_length=256)  
    price: float

class Order(BaseModel):
    id: int
    user_id: int
    item_id: int
    order_date: datetime  
    status: str = Field(max_length=32)

app = FastAPI()

@app.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(
            name=f'user{i}',
            email=f'mail{i}@mail.ru'
            )
        await database.execute(query)
    return {'message': f'{count} fake users create'}

@app.get("/fake_items/{count}")
async def create_items(count: int):
    for i in range(count):
        query = items.insert().values(
            name=f'item{i}',                                      
            description=f'super description{i}', 
            price = randint(10,1000)
            )
        await database.execute(query)
    return {'message': f'{count} fake items create'}

@app.get("/fake_orders/{count}")
async def create_orders(count: int):
    for i in range(count):
        user_id = randint(1, 10) 
        item_id = randint(1, 10)
        order_date = datetime.now()
        status = "pending"
        
        query = orders.insert().values(
            user_id=user_id,
            item_id=item_id,
            order_date=order_date,
            status=status,
        )
        await database.execute(query)
        
    return {'message': f'{count} fake orders created'}

# создание пользователя
@app.post("/users/", response_model=User) 
async def create_user(user: UserIn):
    query = users.insert().values(name=user.name, email=user.email)
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}

@app.post("/items/", response_model=Item) 
async def create_item(item: ItemIn):
    query = items.insert().values(
            name=item.name,                                      
            description=item.description, 
            price = item.price
            )
    return {**item.dict()}

@app.post("/orders/", response_model=Order)
async def create_order(order: OrderIn):
    query = orders.insert().values(
        user_id=order.user_id,
        item_id=order.item_id,
        description=order.description,
        order_date=datetime.now(),  
        status="pending" 
    )
    last_record_id = await database.execute(query)
    return {**order.dict(), "id": last_record_id}

@app.get("/users/", response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)

@app.get("/items/", response_model=List[Item])
async def read_items():
    query = items.select()
    return await database.fetch_all(query)

@app.get("/orders/", response_model=List[Order])
async def read_orders():
    query = orders.select()
    return await database.fetch_all(query)

# чтение одного пользователя
@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    query = items.select().where(items.c.id == item_id)
    return await database.fetch_one(query)

@app.get("/orders/{order_id}", response_model=Order)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)

@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}

@app.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: int, new_order: OrderIn):
    query = orders.update().where(orders.c.id == order_id).values(**new_order.dict())
    await database.execute(query)
    return {**new_order.dict(), "id": order_id}

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, new_item: ItemIn):
    query = items.update().where(items.c.id == item_id).values(**new_item.dict())
    await database.execute(query)
    return {**new_item.dict(), "id": item_id}

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}

@app.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {'message': 'Order deleted'}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    query = items.delete().where(items.c.id == item_id)
    await database.execute(query)
    return {'message': 'Item deleted'}

