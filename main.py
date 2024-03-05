from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str


tasks = []

for i in range(0, 11):
    new_task = Task(
        id=i,
        title=f'title + {i}',
        description=f'description + {i}',
        status=f'status + {i}')
    tasks.append(new_task)


@app.get("/tasks")
async def get_tasks():
    return tasks


@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    return {"message": "task not found"}


@app.post("/task")
async def create_task(task: Task):
    tasks.append(task)
    return tasks


@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: Task):
    for task in tasks:
        if task.id == task_id:
            task.title = task.title
            task.description = task.description
            task.status = task.status
            return task
    return {"message": "task not found"}


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {"message": "task removed"}
    return {"message": "task not found"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)