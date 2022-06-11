import inspect
import types
import builtins
import importlib
from serializer.pack_recover import type_lists


class PackObj:

    def __init__(self):
        self.mod = importlib.import_module(__name__)

    def pack_obj(self, obj):
        packed_obj = {}
        type_obj = type(obj)

        if type_obj in type_lists.primitives:
            if isinstance(obj, int):
                packed_obj["type"] = "int"
            elif isinstance(obj, float):
                packed_obj["type"] = "float"
            elif isinstance(obj, bool):
                packed_obj["type"] = "bool"
            elif isinstance(obj, str):
                packed_obj["type"] = "str"
            packed_obj["data"] = obj
            
        elif type_obj in type_lists.collects:
            if isinstance(obj, dict):
                packed_obj["type"] = "dict"
                packed_obj["data"] = {key: self.pack_obj(val) for key, val in obj.items()}
            else:
                if isinstance(obj, list):
                    packed_obj["type"] = "list"
                elif isinstance(obj, tuple):
                    packed_obj["type"] = "tuple"
                elif isinstance(obj, list):
                    packed_obj["type"] = "set"
                elif isinstance(obj, set):
                    packed_obj["type"] = "set"
                elif isinstance(obj, frozenset):
                    packed_obj["type"] = "frozenset"
                packed_obj["data"] = [self.pack_obj(el) for el in obj]
            
        elif type_obj in type_lists.bytes_obj:
            if isinstance(obj, bytes):
                packed_obj["type"] = "bytes"
            if isinstance(obj, bytearray):
                packed_obj["type"] = "bytearray"
            packed_obj["data"] = [byte for byte in obj]
            
        elif isinstance(obj, types.CodeType):
            packed_obj["type"] = "codeobject"
            packed_obj["data"] = self.pack_obj(self.get_coattrs(obj))
            
        elif isinstance(obj, types.FunctionType):
            packed_obj["type"] = "function"
            packed_obj["data"] = self.pack_obj(self.pack_func(obj))
            
        elif isinstance(obj, types.BuiltinFunctionType):
            packed_obj["type"] = "builtinfunction"
            packed_obj["data"] = self.pack_obj(self.pack_builtinfunc(obj))
            
        elif isinstance(obj, types.CellType):
            packed_obj["type"] = "celltype"
            packed_obj["data"] = self.pack_obj(obj.cell_contents)
            
        elif isinstance(obj, type):
            packed_obj["type"] = "class"
            packed_obj["data"] = self.pack_obj(self.pack_class(obj))
            
        elif self.is_class_instance(obj):
            packed_obj["type"] = "instance"
            packed_obj["data"] = self.pack_obj(self.pack_instance(obj))

        return packed_obj

    def pack_func(self, obj):
        packed_obj = {}
        globs = {}
        # Посмотреть при замене на name
        obj_attrs = {"__name__": obj.__qualname__,
                     "__defaults__": obj.__defaults__,
                     "__closure__": obj.__closure__,
                     "__code__": obj.__code__}
        self.get_globs(obj, globs)
        packed_obj["__globals__"] = globs
        packed_obj["attributes"] = obj_attrs
        return packed_obj

    def get_globs(self, obj, globs):
        if hasattr(obj, '__code__'):
            code_obj = obj.__code__
            for constant in code_obj.co_consts:
                self.get_globs(constant, globs)
            for coname in code_obj.co_names:
                if coname in obj.__globals__.keys() and coname != obj.__name__:
                    globs[coname] = obj.__globals__[coname]
                elif coname in dir(builtins):
                    globs[coname] = getattr(builtins, coname)
                    
    def get_coattrs(self, obj):
        co_attrs = {}
        for key in dir(obj):
            if key.startswith("co_"):
                value = obj.__getattribute__(key)
                co_attrs[key] = value
                
        return co_attrs
    
    def pack_builtinfunc(self, obj):
        packed_obj = {"type": "builtinfunction",
                      "module": obj.__module__,
                      "attributes": {"__name__": obj.__name__}}

        return packed_obj
    
    def pack_class(self, obj):
        # Почему именно кортеж, а не список
        packed_obj = {"__name__": obj.__name__,
                      "__bases__": tuple([base for base in obj.__bases__ if base is not object]),
                      "__dict__": dict(obj.__dict__)}
        
        return packed_obj

    def pack_instance(self, obj):
        packed_obj = {"class": obj.__class__,
                      "dict": obj.__dict__}

        return packed_obj

    def is_class_instance(self, obj):
        if not hasattr(obj, "__dict__") or inspect.isroutine(obj) \
                or inspect.isclass(obj) or inspect.ismodule(obj) \
                or not hasattr(obj, '__module__'):
            return False
        else:
            mod = importlib.import_module(obj.__module__)
            if obj.__class__.__name__ not in \
                    dict(inspect.getmembers(mod, inspect.isclass)):
                return False
            else:
                return True
