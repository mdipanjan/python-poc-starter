#!/bin/bash

# Setup script for the project
echo "Setting up the project..."
python -m venv env
source env/bin/activate
pip install -r requirements.txt 