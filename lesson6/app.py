from typing import List
from fastapi import FastAPI
from databases import Database
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = 'sqlite:///./mydatabase.db'
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
session_local = sessionmaker(autocommit = False, autoflush=False, bind=engine)
Base = declarative_base()
database = Database(DATABASE_URL)


class User(BaseModel):
    id: int = Field(default = None, alias = 'user_id')
    username: str = Field(..., title = 'Name', min_length=2, max_length=50)
    email: str = Field(..., title = 'Email', min_length=6, max_length=50)
    password: str = Field(..., title = 'Password', min_length=2, max_length=50)
    
    class Config:
        orm_mode = True
 
class DB_User(Base):
    __tablename__ = 'users'
    id = Column(Integer, ptimary_key = True, index = True)
    username = Column(String(50))
    email = Column(String(50))
    password = Column(String(50))
    

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.on_event('startup')
async def startup():
    await database.connect()
    
@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()

@app.get("/")
async def root():
    return {'message':'Hello world!'}

@app.get('/users/', response_model=List[User])
async def read_users():
    # query = DB_User.__tablename__.select()
    # users = 
    return {'message':'Hello users'}

@app.get('/add_user_fake/')
async def add_user_fake():
    for i in range(20):
        # query = DB_User.__table__.
        return