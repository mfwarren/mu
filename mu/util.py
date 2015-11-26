import sys

from mu.errors import AppImportError

def import_app(module):
    parts = module.split(":", 1)
    if len(parts) == 1:
        module, obj = module, "application"
    else:
        module, obj = parts[0], parts[1]

    try:
        __import__(module)
    except ImportError:
        if module.endswith(".py") and os.path.exists(module):
            msg = "Failed to find application, did you mean '%s:%s'?"
            raise ImportError(msg % (module.rsplit(".", 1)[0], obj))
        else:
            raise

    mod = sys.modules[module]

    try:
        app = eval(obj, mod.__dict__)
    except NameError:
        raise AppImportError("Failed to find application: %r" % module)

    if app is None:
        raise AppImportError("Failed to find application object: %r" % obj)

    return app
