import yaml


def read_config():
    return yaml.load(open('3xagent.yml', 'r'))

def save_config(config):
    yaml.dump(config, open('3xagent.yml', 'w'), default_flow_style=False)
