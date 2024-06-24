#!/bin/bash

app_name="Tail Node Site"

echo "Creating a $app_name virtual environment..."
python3.12 -m venv venv

if [ -d "venv" ]; then
    echo "Virtual environment created successfully."
else
    echo "Error: Failed to create virtual environment."
    exit 1
fi

source venv/bin/activate

if [ "$VIRTUAL_ENV" != "" ]; then
    echo "$app_name virtual environment activated."
else
    echo "Error: $app_name virtual environment activation failed."
    exit 1
fi

echo "Installing the latest version of pip..."
python -m pip install --upgrade pip
if [ $? -ne 0 ]; then
    echo "Error: Failed to upgrade pip."
    exit 1
fi

echo "Installing project requirements..."
python -m pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Error: Failed to install requirements."
    exit 1
fi

echo "Initializing $app_name database..."
python manage.py migrate
if [ $? -ne 0 ]; then
    echo "Error: Failed to initialize database."
    exit 1
fi

echo "Collecting static files..."
python manage.py collectstatic --noinput
if [ $? -ne 0 ]; then
    echo "Error: Failed to collect static files."
    exit 1
fi

echo "Build completed successfully."