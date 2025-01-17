# Author: Mikel Valencia
# 

import pathlib
from typing import Annotated, Any, Literal
from pydantic import AnyUrl, BeforeValidator, computed_field

from pydantic_settings import BaseSettings, SettingsConfigDict


def parse_cors(v: Any) -> list[str] | str:
    """Function to parse the CORS received from client."""
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)


class Settings(BaseSettings):

    # Read .env file.
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )

    PROJECT_NAME: str
    ENVIRONMENT: Literal["local", "production"] = "local"

    API_V1_STR: str = "/api/v1"
    FRONTEND_HOST: str = "http://localhost:5173"

    # Define allowed CORS origins.
    BACKEND_CORS_ORIGINS: Annotated[
        list[AnyUrl] | str, BeforeValidator(parse_cors)
    ] = []

    @computed_field
    @property
    def all_cors_origins(self) -> list[str]:
        """Return a list with all allowed CORS origins, including the frontend host."""
        return [str(origin).rstrip("/") for origin in self.BACKEND_CORS_ORIGINS] + [
            self.FRONTEND_HOST
        ]

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        """Return the database connection URL."""
        return f"sqlite:///{pathlib.Path(__file__).parents[2].resolve()}/myhealthassistant.db"
    

# Create the settings global variable.
settings = Settings()
