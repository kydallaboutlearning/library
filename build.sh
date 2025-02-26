#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run tests
echo "Running tests..."
python manage.py test

echo "Build process completed successfully!"