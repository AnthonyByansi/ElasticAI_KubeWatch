#!/bin/bash

# ElasticAI KubeWatch - Docker Image Build Script

# Set the Docker image name and tag
DOCKER_IMAGE_NAME="elasticai-kubewatch"
DOCKER_IMAGE_TAG="latest"

# Build the Docker image
docker build -t $DOCKER_IMAGE_NAME:$DOCKER_IMAGE_TAG .

# Tag the Docker image for Azure Container Registry
ACR_NAME="your-acr-name"  # Replace with your ACR name
docker tag $DOCKER_IMAGE_NAME:$DOCKER_IMAGE_TAG $ACR_NAME.azurecr.io/$DOCKER_IMAGE_NAME:$DOCKER_IMAGE_TAG

# Authenticate to Azure Container Registry
az acr login --name $ACR_NAME

# Push the Docker image to Azure Container Registry
docker push $ACR_NAME.azurecr.io/$DOCKER_IMAGE_NAME:$DOCKER_IMAGE_TAG

# Clean up by removing locally built image
docker image rm $DOCKER_IMAGE_NAME:$DOCKER_IMAGE_TAG
docker image rm $ACR_NAME.azurecr.io/$DOCKER_IMAGE_NAME:$DOCKER_IMAGE_TAG

echo "Docker image build and push completed."
