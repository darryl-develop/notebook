import yaml

# Load YAML file
with open('config.yml') as yml:
	config=yaml.load(yml)

# Save YAML file
with open("new-config.yml", 'w') as ymlfile:
    yaml.dump(config, ymlfile,default_flow_style=False)
