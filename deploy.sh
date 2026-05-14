#!/bin/bash

echo "Stopping old containers..."
docker compose down

echo "Building containers..."
docker compose build

echo "Starting application..."
docker compose up -d

echo "Application deployed successfully!"