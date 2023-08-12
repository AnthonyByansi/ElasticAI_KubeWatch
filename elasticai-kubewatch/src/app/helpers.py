import os
import yaml

def load_config(file_path):
    with open(file_path, "r") as config_file:
        config = yaml.safe_load(config_file)
    return config

def calculate_scaling_factor(metric_value, scaling_rules):
    scaling_factor = 1.0
    for rule in scaling_rules:
        if rule["operator"] == "greater_than" and metric_value > rule["threshold"]:
            scaling_factor *= rule["scale_factor"]
        elif rule["operator"] == "less_than" and metric_value < rule["threshold"]:
            scaling_factor *= rule["scale_factor"]
    return scaling_factor

def get_environment_variable(variable_name, default_value=None):
    return os.environ.get(variable_name, default_value)
