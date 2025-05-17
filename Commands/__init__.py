import importlib
import pkgutil

def load_all_builtins():
    import Commands 
    package = Commands
    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        importlib.import_module(f"{package.__name__}.{module_name}")