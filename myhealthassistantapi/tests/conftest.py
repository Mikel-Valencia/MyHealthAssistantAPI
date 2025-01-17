# Author: Mikel Valencia

from collections.abc import Generator
import pytest
from fastapi.testclient import TestClient
from sqlmodel import create_engine, Session, SQLModel
from sqlmodel.pool import StaticPool

from myhealthassistantapi.main import app
from myhealthassistantapi.api.deps import get_db


@pytest.fixture(scope="session")
def testing_db() -> Generator[Session, None, None]:
    """Fixture that creates a testing database independent from production database."""
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(scope="module")
def client(testing_db: Session) -> Generator[TestClient, None, None]:
    """
    Fixture that creates a testing client and overrrides the production database
    with the testing database using dependency injection.
    """
    def get_testing_db():
        return testing_db
    app.dependency_overrides[get_db] = get_testing_db
    client = TestClient(app)  
    yield client  
    app.dependency_overrides.clear()
