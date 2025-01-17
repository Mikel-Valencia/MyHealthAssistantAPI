# Author: Mikel Valencia
# Define some dependencies used in the API.

from collections.abc import Generator
from typing import Annotated
from fastapi import Depends
from sqlmodel import Session

from myhealthassistantapi.core.db import engine


def get_db() -> Generator[Session, None, None]:
    """Get the database instance."""
    with Session(engine) as session:
        yield session


# Database session dependency.
SessionDep = Annotated[Session, Depends(get_db)]
