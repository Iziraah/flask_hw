# from os import path
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List

app = FastAPI
templates = Jinja2Templates(directory='templates')

class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str
    
tasks = []

for i in range(1, 10):
    tasks.append(Task(id=i, title = f'Title{i}', description=f'Description{i}', status=f'Status{i}'))
    
@app.get("/", response_class=HTMLResponse)
async def read_tasks(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'tasks': tasks})

@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    return tasks

@app.post("/tasks", response_model=Task)
async def create_tasks(task: Task):
    task.id = len(tasks) + 1
    tasks.append(task)
    return task

@app.put("/tasks/{task_id}", response_model=Task)
async def update_tasks(task_id: int, task: Task):
    for i in range(len(tasks)):
        if tasks[i].id == task_id:
            task.id = task_id
            tasks[i] = task
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
async def delete_tasks(task_id: int):
    for i in range(len(tasks)):
        if tasks[i].id == task_id:
            del tasks[i]
            return {"messeage": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")