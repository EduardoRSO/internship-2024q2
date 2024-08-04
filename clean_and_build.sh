#!/bin/sh

# Stop all running containers
echo "Stopping all running containers..."
docker stop $(docker ps -a -q)

# Remove all containers
echo "Removing all containers..."
docker rm $(docker ps -a -q)

# Forcefully remove all images
echo "Removing all Docker images..."
docker rmi -f $(docker images -q)

# Build the Docker image
echo "Building the Docker image..."
docker build -t my-lambda-function .

# Run the Docker container
echo "Running the Docker container..."
docker run -p 9000:8080 my-lambda-function
