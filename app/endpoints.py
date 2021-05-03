from fastapi import APIRouter, Response, status
from fastapi.responses import JSONResponse
from celery.result import AsyncResult
from .celery import app

router = APIRouter()
from app import tasks


@router.get("/")
async def start(response: Response):
    task = tasks.add.s(2, 3).apply_async()
    content = {"id": task.id}
    headers = {"Location": f"/{task.id}/status"}
    return JSONResponse(
        status_code=status.HTTP_202_ACCEPTED, content=content, headers=headers
    )


@router.get("/{task_id}/status")
async def task_status(task_id: str):
    task = AsyncResult(task_id, app=app)
    content = {"status": task.state}
    headers = {
        "Location": f"/{task.id}/status",
        "Retry-After": "5",
        "Cache-Control": "no-cache",
    }
    status_code = status.HTTP_202_ACCEPTED

    if task.state == "SUCCESS":
        headers = {"Location": f"/{task.id}/result"}
        status_code = status.HTTP_302_FOUND

    return JSONResponse(status_code=status_code, content=content, headers=headers)


@router.get("/{task_id}/result")
async def result(task_id: str):
    res = AsyncResult(task_id, app=app)
    return {"result": res.get()}
