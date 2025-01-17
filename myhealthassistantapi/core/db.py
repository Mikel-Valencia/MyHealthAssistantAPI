# Author: Mikel Valencia

from sqlmodel import Session, create_engine

from myhealthassistantapi.core.config import settings
from myhealthassistantapi.models import Food


engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))


def init_db(session: Session) -> None:
    """Initialize database. Creates tables and a first superuser in database's first initialization."""
    
    from sqlmodel import SQLModel

    SQLModel.metadata.create_all(engine)
