# Author: Mikel Valencia
# Nutrition API routes.

from typing import Any
from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from myhealthassistantapi.api.deps import SessionDep
from myhealthassistantapi.models import Food, FoodPublic, FoodsPublic


router = APIRouter(prefix="/nutrition", tags=["nutrition"])


@router.get("/", response_model=FoodsPublic)
def read_foods(session: SessionDep, skip: int = 0, limit: int = 100) -> Any:
    """Get food data."""

    count_statement = select(func.count()).select_from(Food)
    count = session.exec(count_statement).one()
    statement = select(Food).offset(skip).limit(limit)
    foods = session.exec(statement).all()

    return FoodsPublic(data=foods, count=count)


@router.get("/{id}", response_model=FoodPublic)
def read_food(session: SessionDep, id: int) -> Any:
    """Get food data by id."""

    food = session.get(Food, id)
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")

    return food
