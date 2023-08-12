#!/bin/bash

# ElasticAI KubeWatch - Deploy to AKS Script

# Set your AKS cluster name
AKS_CLUSTER_NAME="your-aks-cluster-name"

# Deploy the Azure Functions
az functionapp deployment source config-zip --name elasticai-kubewatch-func --resource-group your-resource-group --src ./src/app/azure_functions.zip

# Deploy the Kubernetes manifests
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/autoscaler.yaml

echo "Deployment to AKS completed."
