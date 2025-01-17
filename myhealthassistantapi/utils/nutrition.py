# Author: Mikel Valencia

from sqlmodel import Session

from myhealthassistantapi.models import Food, FoodCreate


def create_food(*, session: Session, food_in: FoodCreate) -> Food:
    db_item = Food.model_validate(food_in)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item
