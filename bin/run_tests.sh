#!/usr/bin/env bash

# move to project repo (absolute).
cd "$(dirname $(dirname $0))"

source ./venv/bin/tests

pytest tests
