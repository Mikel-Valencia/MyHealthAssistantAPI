# Author: Mikel Valencia

from sqlmodel import Session

from myhealthassistantapi.models import Food, FoodCreate
from myhealthassistantapi.utils import create_food
from myhealthassistantapi.tests.utils.utils import random_lower_string, random_fraction, random_positive_float


def create_random_food(db: Session) -> Food:
    food_in = FoodCreate(
        name=random_lower_string(),
        portion=random_fraction(),
        energy=random_positive_float(),
        carbohydrates=random_positive_float(),
        proteins=random_positive_float(),
        fat=random_positive_float(),
    )
    return create_food(session=db, food_in=food_in)
