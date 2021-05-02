from importlib import import_module
import sys
import config


class Handler:
    def __init__(self, call, type, params=None):
        self.call = call
        self.params = params
        self.type = type

    def handle(self):
        sys.path.append(config.server["calculatorsPath"]+self.type)
        module = import_module(self.call + ".main")
        module_class = getattr(module, self.call)
        instantiate = module_class(self.params)
        return instantiate.get()
