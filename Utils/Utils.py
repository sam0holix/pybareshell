import os

def find_executable_in_path(command_name: str) -> str | None:
    path_variable = os.environ.get('PATH', '')
    directories = path_variable.split(os.pathsep)

    for directory in directories:
        full_path = os.path.join(directory, command_name)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return full_path

    return None