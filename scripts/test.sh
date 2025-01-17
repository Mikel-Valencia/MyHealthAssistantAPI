#!/usr/bin/env bash

set -e
set -x

source venv/Scripts/activate

coverage run --source=myhealthassistantapi -m pytest
coverage report --show-missing
coverage html --title "${@-coverage}"
