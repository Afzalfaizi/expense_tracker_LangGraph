from fastapi import FastAPI,Depends ,HTTPException
from ..crud.crud import create_expense,get_expense_by_id,get_expenses
from ..database.db import get_session
from typing import Annotated
from sqlmodel import Session
from ..models.model import ExpenseBase
from fastapi import APIRouter


router = APIRouter()

@router.get("/expenses")
async def get_all_expenses(session:Annotated[Session,Depends(get_session)]):
    data =  get_expenses(session=session)
    return data 

@router.get("/expenses/{expense_id}")
async def get_expense(expense_id: int,session:Annotated[Session,Depends(get_session)]):
        data = get_expense_by_id(session=session,expense_id=expense_id)
        return data

@router.post("/expenses")
async def create_expenses(session:Annotated[Session,Depends(get_session)],expense:ExpenseBase):
    data = create_expense(session=session,expense=expense)
    return data