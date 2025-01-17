# Author: Mikel Valencia
# Collect all APIRouter classes from routes package and merge them into a single APIRouter class.
# This global APIRouter will be added to the myhealthassistantapi/main.py app router.

from fastapi import APIRouter

from myhealthassistantapi.api.routes import nutrition, utils


api_router = APIRouter()
api_router.include_router(nutrition.router)
api_router.include_router(utils.router)
