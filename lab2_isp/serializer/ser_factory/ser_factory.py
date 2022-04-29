from serializer.json_serializer import json_serializer as json
from serializer.toml_serializer import toml_serializer as toml
from serializer.yaml_serializer import yaml_serializer as yaml


class SerFactory:
    def __init__(self, path: str):
        self.path = path

    def create_serializer(self, extension="json"):
        if extension.lower() == "json":
            return json.JsonSerializer(self.path)
        elif extension.lower() == "toml":
            return toml.TomlSerializer(self.path)
        elif extension.lower() == "yaml":
            return yaml.YamlSerializer(self.path)
