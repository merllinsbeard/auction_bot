import yaml
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
conf = os.path.join(current_dir, "..", "..", "config.yaml")

with open(conf, "r") as conf_file:
    data = yaml.safe_load(conf_file)
    TOKEN_CRYPTO = data.get("CRYPTOBOTTOKEN")
