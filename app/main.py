from fastapi import FastAPI
from contextlib import asynccontextmanager
from .database.db import create_table
from .route.route import router

from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_table()
    print("Starting up")
    yield
    # Shutdown l

app = FastAPI(lifespan=lifespan)


@app.get("/")
async def read_root():
    return {"Expense Tracker App with LangGraph"}


app.include_router(router=router, prefix="/api", tags=["api"])