import json
import os

"""
In config files ":var1" indicates that the value will check in the following order: 
    instance_configuration
    runtime_configuration
    base_configuration
    
    Configurations are JSON dicts with key value pairs
    
    {"key": "value"}
    
    [
        {"action": "run",
         "project": "agile_data_tools",
         "script": "./bulk_import_import_script.py",
         "parameters": {}
        }
    
    ]
    
"""


class Configuration(object):
    def __init__(self, config):
        self.config = config


class Project(object):
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.interpreter_obj = None

    def register_python(self, interpreter_obj):
        self.interpreter_obj = interpreter_obj

    def register_script(self, relative_path_to_script):
        pass

    def run_script(self, relative_path_to_script):
        pass


class PythonInterpreter(object):
    def __init__(self, name, path_to_interpreter):
        self.name = name
        self.path_to_interpreter = path_to_interpreter


class DatabaseConnection(object):
    def __init__(self, name, connection_uri):
        self.name = name
        self.connection_uri - connection_uri


class BaseConfiguration(Configuration):
    pass


class RuntimeConfiguration(Configuration):
    pass


class InstanceConfiguration(Configuration):
    pass


class CommandScript(object):
    def __init__(self, path_to_command):
        pass

    def run(self, args):
        pass


class PythonCommandScript(CommandScript):
    def __init__(self, path_to_python_script):
        self.path_to_python_script = path_to_python_script

    def run(self, args):
        pass


class RunEnvironment(object):
    def __init__(self, base_configuration, runtime_configuration, instance_configuration):
        self.base_configuration = base_configuration
        self.runtime_configuration = runtime_configuration
        self.instance_configuration = instance_configuration

        self.projects_dict = {}

    def register_projects(self, project_objs):

        if project_objs.__class__ not in ([].__class__, ().__class__):
            project_objs = [project_objs]

        for project_obj in project_objs:
            self.project_dict[project_obj.name] = project_obj


class ConfigurationFile(object):
    pass


class JSONConfigurationFile(object):

    def __init__(self, json_config_file_name, config_obj):
        self.config_obj = config_obj
        self.evaluated_config_obj = config_obj
        self.json_config_file_name = json_config_file_name

    def write(self, path, evaluate_dict):
        pass


class EvaluateConfiguration(object):
    pass