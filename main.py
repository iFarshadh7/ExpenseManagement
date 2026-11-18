from fastapi import FastAPI, HTTPException, status, Response
from pydantic import BaseModel, Field

app = FastAPI(
    title="Expense Management API",
    description="A simple API for managing expenses",
    version="1.0.0"
)

expenses = {}


class ExpenseCreate(BaseModel):
    description: str = Field(min_length=1)
    amount: float = Field(gt=0)


@app.post("/expenses/",status_code=status.HTTP_201_CREATED)
def create_expense(expense: ExpenseCreate):
    new_id = max(expenses.keys(), default=0) + 1
    new_expense = {
        "id": new_id,
        "description": expense.description,
        "amount": expense.amount
    }

    expenses[new_id] = new_expense

    return new_expense


@app.get("/expenses/")
def get_all_expenses():
    return list(expenses.values())


@app.get("/expenses/{expense_id}")
def get_expense(expense_id: int):

    if expense_id not in expenses:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expense not found"
        )

    return expenses[expense_id]


@app.put("/expenses/{expense_id}")
def update_expense(
    expense_id: int,
    expense: ExpenseCreate
):

    if expense_id not in expenses:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expense not found"
        )

    updated_expense = {
        "id": expense_id,
        "description": expense.description,
        "amount": expense.amount
    }

    expenses[expense_id] = updated_expense

    return updated_expense


@app.delete(
    "/expenses/{expense_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_expense(expense_id: int):

    if expense_id not in expenses:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expense not found"
        )

    del expenses[expense_id]

    return Response(status_code=status.HTTP_204_NO_CONTENT)
