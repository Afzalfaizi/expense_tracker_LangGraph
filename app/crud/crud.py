from sqlmodel import Session,select
from ..models.model import Expense, ExpenseBase
from ..database.db import get_session
from typing import Annotated
from fastapi import Depends, HTTPException, status


def create_expense(session:Annotated[Session, Depends(get_session)], expense: ExpenseBase) -> Expense:
    db_expense = Expense(**expense.dict())
    session.add(db_expense)
    session.commit()
    session.refresh(db_expense)
    return db_expense



def get_expenses(session: Session):
    data = session.exec(select(Expense)).all()
    return data

def get_expense_by_id(session: Session, expense_id: int) :
    data = session.exec(select(Expense).where(Expense.id == expense_id)).first()
    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense Not Found")
    return data