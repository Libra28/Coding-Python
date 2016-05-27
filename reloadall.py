"""
reloadall.py: transitively reload nested modules
"""

import types
from imp import reload

def status(module):
    print('reloading '+ module._name_)

def transitive_reload(module,visited):
    if not module in visited:
        status(module)
        reload(module)
        visited[module] = None
        for attrobj in module._dict_.values:
            if type(attrobj) == types.ModuleType:
                transitive_reload(attrobj,visited)

def reload_all(*args):
    visited = {}
    for arg in args:
        if type(arg) == types.ModuleType:
            transitive_reload(arg,visited)

if _name_ =='_main_':
    import reloadall
    reload_all(reloadall)
