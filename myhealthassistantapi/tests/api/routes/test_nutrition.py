# Author: Mikel Valencia

from decimal import Decimal
from fastapi.testclient import TestClient
from sqlmodel import Session

from myhealthassistantapi.core.config import settings
from myhealthassistantapi.tests.utils.nutrition import create_random_food


def test_read_food(client: TestClient, testing_db: Session) -> None:
    food = create_random_food(testing_db)
    response = client.get(f"{settings.API_V1_STR}/nutrition/{food.id}")
    assert response.status_code == 200
    content = response.json()
    assert content["id"] == food.id
    assert content["name"] == food.name
    assert Decimal(content["portion"]) == food.portion
    assert Decimal(content["energy"]) == food.energy
    assert Decimal(content["carbohydrates"]) == food.carbohydrates
    assert Decimal(content["proteins"]) == food.proteins
    assert Decimal(content["fat"]) == food.fat


def test_read_food_not_found(client: TestClient) -> None:
    response = client.get(f"{settings.API_V1_STR}/nutrition/0")
    assert response.status_code == 404
    content = response.json()
    assert content["detail"] == "Food not found"


def test_read_foods(client: TestClient, testing_db: Session) -> None:
    create_random_food(testing_db)
    create_random_food(testing_db)
    response = client.get(f"{settings.API_V1_STR}/nutrition/")
    assert response.status_code == 200
    content = response.json()
    assert len(content["data"]) >= 2
    assert content["count"] >= 2
