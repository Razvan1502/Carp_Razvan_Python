import json

def parse_config(config_file):
    # Parse configuration from JSON file
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config
