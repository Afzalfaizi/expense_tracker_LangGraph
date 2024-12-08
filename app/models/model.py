from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship


# SQLModel for Expense Table
class Expense(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    description: str
    amount: float
    date: datetime = Field(default_factory=datetime.utcnow)
    category: str


# Schema for creating and reading expenses
class ExpenseBase(BaseModel):
    description: str
    amount: float
    date: datetime = Field(default_factory=datetime.utcnow)  # Default factory for date
    category: str

# Schema for updating existing expenses
class ExpenseUpdate(BaseModel):
    description: Optional[str] = None
    amount: Optional[float] = None
    date: Optional[datetime] = None  # Should accept datetime for flexibility
    category: Optional[str] = None