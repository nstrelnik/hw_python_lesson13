import os
import tests


def path(file_name):
    return os.path.join(os.path.dirname(tests.__file__), f"./resource/{file_name}")
