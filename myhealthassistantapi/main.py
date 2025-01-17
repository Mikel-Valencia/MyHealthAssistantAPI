# Author: Mikel Valencia
# myhealthassistantapi/main.py defines the main entrypoint to use the API.

from fastapi import FastAPI
from fastapi.routing import APIRoute
from starlette.middleware.cors import CORSMiddleware

from myhealthassistantapi.api.main import api_router
from myhealthassistantapi.core.config import settings


# Customize the function used to generate unique IDs for the path operations shown in the generated OpenAPI.
def custom_generate_unique_id(route: APIRoute):
    return f"{route.tags[0]}-{route.name}"


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",  # The URL where the OpenAPI schema will be served from.
    generate_unique_id_function=custom_generate_unique_id
)


# Set all CORS enabled origins.
# https://fastapi.tiangolo.com/tutorial/cors/
if settings.all_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.all_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


# Include the APIRouter in the same current APIRouter.
app.include_router(api_router, prefix=settings.API_V1_STR)
