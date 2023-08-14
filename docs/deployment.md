# ⚙️ Deployment

This guide provides step-by-step instructions to deploy the ElasticAI KubeWatch solution on Azure Kubernetes Service (AKS). 🚀

## 📋 Prerequisites

Before proceeding with the deployment, ensure you have the following prerequisites:

- An active Azure subscription.
- Azure CLI installed and configured with the correct subscription: [Install Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli).
- Access to create resources in the target Azure subscription, such as AKS, Azure Functions, etc.
- Docker installed on your local machine to build the container image.

## 🚀 Deployment Steps

1. **Create AKS Cluster**:
   - Use Azure CLI to create an AKS cluster with the desired configuration:
     ```bash
     az aks create --resource-group <resource-group-name> --name <aks-cluster-name> --node-count <node-count> --node-vm-size <vm-size> --enable-addons monitoring --generate-ssh-keys
     ```

2. **Deploy Azure Functions**:
   - Create an Azure Functions App using Azure CLI:
     ```bash
     az functionapp create --resource-group <resource-group-name> --name <function-app-name> --storage-account <storage-account-name> --consumption-plan-location <region>
     ```
   - Deploy the Azure Functions code to the created app:
     ```bash
     func azure functionapp publish <function-app-name> --python
     ```

3. **Configure Kubernetes**:
   - Set up the Kubernetes configuration for AKS:
     ```bash
     az aks get-credentials --resource-group <resource-group-name> --name <aks-cluster-name>
     ```

4. **Build and Push Docker Image**:
   - Build the Docker image for the ElasticAI KubeWatch application:
     ```bash
     docker build -t <docker-image-name> .
     ```
   - Tag the Docker image for your Azure Container Registry (ACR):
     ```bash
     docker tag <docker-image-name> <acr-name>.azurecr.io/<docker-image-name>:<tag>
     ```
   - Push the Docker image to ACR:
     ```bash
     az acr login --name <acr-name>
     docker push <acr-name>.azurecr.io/<docker-image-name>:<tag>
     ```

5. **Deploy the Application**:
   - Apply the Kubernetes Deployment and Service manifests:
     ```bash
     kubectl apply -f kubernetes/deployment.yaml
     kubectl apply -f kubernetes/autoscaler.yaml
     ```

6. **Verify Deployment**:
   - Ensure the application pods are running:
     ```bash
     kubectl get pods
     ```

7. **Monitor Auto-Scaling**:
   - Monitor the ElasticAI KubeWatch application auto-scaling behavior through the Azure Functions and AKS dashboard.

## 📄 Configuration

For customization and configuration of ElasticAI KubeWatch, refer to the [Configuration](config/config.md) guide.

---
