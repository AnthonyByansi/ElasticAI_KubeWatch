# ElasticAI KubeWatch - Main Application

import os
import azure.functions as func
from .kubewatch_functions import KubernetesFunctions
from .helpers import get_environment_variable

def main(event: func.EventGridEvent):
    # Initialize KubernetesFunctions instance
    kubernetes_functions = KubernetesFunctions()

    # Get the metric value from the event payload (replace this with actual event handling)
    metric_value = float(event.get_json().get("metric_value"))

    # Scale based on the metric value
    kubernetes_functions.scale_based_on_metric(metric_value)

    # Log the scaling action
    logging.info(f"Auto-scaled based on metric: {metric_value}")

if __name__ == "__main__":
    # For local testing
    metric_value = float(get_environment_variable("TEST_METRIC_VALUE"))
    main(metric_value)
