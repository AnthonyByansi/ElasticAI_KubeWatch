# ElasticAI KubeWatch - Kubernetes Functions

from kubernetes import client, config
from .helpers import calculate_scaling_factor, load_config

class KubernetesFunctions:
    def __init__(self, config_path="config/config.yaml"):
        self.config = load_config(config_path)
        self.load_kube_config()

    def load_kube_config(self):
        config.load_kube_config()

    def get_pod_replicas(self, deployment_name):
        api_instance = client.AppsV1Api()
        response = api_instance.read_namespaced_deployment_scale(
            name=deployment_name, namespace=self.config["namespace"]
        )
        return response.spec.replicas

    def set_pod_replicas(self, deployment_name, replicas):
        api_instance = client.AppsV1Api()
        scale = client.V1Scale(
            spec=client.V1ScaleSpec(replicas=replicas),
        )
        api_instance.replace_namespaced_deployment_scale(
            name=deployment_name,
            namespace=self.config["namespace"],
            body=scale,
        )

    def adjust_replicas(self, deployment_name, scaling_factor):
        current_replicas = self.get_pod_replicas(deployment_name)
        new_replicas = int(current_replicas * scaling_factor)
        new_replicas = max(new_replicas, self.config["min_replicas"])
        new_replicas = min(new_replicas, self.config["max_replicas"])
        self.set_pod_replicas(deployment_name, new_replicas)

    def scale_based_on_metric(self, metric_value):
        scaling_factor = calculate_scaling_factor(
            metric_value, self.config["scaling_rules"]
        )
        deployment_name = self.config["deployment_name"]
        self.adjust_replicas(deployment_name, scaling_factor)

# Create an instance of KubernetesFunctions
kubernetes_functions = KubernetesFunctions()
