#!/usr/bin/env bash

set -e
set -x

source venv/Scripts/activate

fastapi dev myhealthassistantapi/main.py