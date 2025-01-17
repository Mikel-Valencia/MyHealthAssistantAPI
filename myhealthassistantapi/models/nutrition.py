# Author: Mikel Valencia
# Nutrition API models.

from typing import Optional
from decimal import Decimal
from sqlmodel import Field, SQLModel


# Shared properties.
class FoodBase(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)  # Optional in Python code for convenience.
    name: str = Field(min_length=1, nullable=False, max_length=255)
    portion: Decimal = Field(nullable=False, gt=0, le=1, max_digits=3, decimal_places=2)
    energy: Decimal = Field(nullable=False, ge=0, decimal_places=2)
    carbohydrates: Decimal = Field(nullable=False, ge=0, decimal_places=2)
    proteins: Decimal = Field(nullable=False, ge=0, decimal_places=2)
    fat: Decimal = Field(nullable=False, ge=0, decimal_places=2)
    saturated_fat: Optional[Decimal] = Field(default=None, nullable=True, ge=0, decimal_places=2)
    monounsaturated_fat: Optional[Decimal] = Field(default=None, nullable=True, ge=0, decimal_places=2)
    polyunsaturated_fat: Optional[Decimal] = Field(default=None, nullable=True, ge=0, decimal_places=2)
    cholesterol: Optional[Decimal] = Field(default=None, nullable=True, ge=0, decimal_places=2)
    fibre: Optional[Decimal] = Field(default=None, nullable=True, ge=0, decimal_places=2)
    water: Optional[Decimal] = Field(default=None, nullable=True, ge=0, decimal_places=2)
    calcium: Optional[Decimal] = Field(default=None, nullable=True, ge=0, decimal_places=2)
    iron: Optional[Decimal] = Field(default=None, nullable=True, ge=0, decimal_places=2)
    iodine: Optional[Decimal] = Field(default=None, nullable=True, ge=0, decimal_places=2)
    magnesium: Optional[Decimal] = Field(default=None, nullable=True, ge=0, decimal_places=2)
    zinc: Optional[Decimal] = Field(default=None, nullable=True, ge=0, decimal_places=2)
    sodium: Optional[Decimal] = Field(default=None, nullable=True, ge=0, decimal_places=2)
    potassium: Optional[Decimal] = Field(default=None, nullable=True, ge=0, decimal_places=2)
    phosphorus: Optional[Decimal] = Field(default=None, nullable=True, ge=0, decimal_places=2)
    selenium: Optional[Decimal] = Field(default=None, nullable=True, ge=0, decimal_places=2)
    thiamine: Optional[Decimal] = Field(default=None, nullable=True, ge=0, decimal_places=2)
    riboflavin: Optional[Decimal] = Field(default=None, nullable=True, ge=0, decimal_places=2)
    niacin_equivalents: Optional[Decimal] = Field(default=None, nullable=True, ge=0, decimal_places=2)
    vitamin_b6: Optional[Decimal] = Field(default=None, nullable=True, ge=0, decimal_places=2)
    folates: Optional[Decimal] = Field(default=None, nullable=True, ge=0, decimal_places=2)
    vitamin_b12: Optional[Decimal] = Field(default=None, nullable=True, ge=0, decimal_places=2)
    vitamin_c: Optional[Decimal] = Field(default=None, nullable=True, ge=0, decimal_places=2)
    vitamin_a: Optional[Decimal] = Field(default=None, nullable=True, ge=0, decimal_places=2)
    vitamin_d: Optional[Decimal] = Field(default=None, nullable=True, ge=0, decimal_places=2)
    vitamin_e: Optional[Decimal] = Field(default=None, nullable=True, ge=0, decimal_places=2)


class FoodCreate(FoodBase):
    pass


class Food(FoodBase, table=True):
    pass


class FoodPublic(FoodBase):
    pass


class FoodsPublic(SQLModel):
    data: list[FoodPublic]
    count: int

