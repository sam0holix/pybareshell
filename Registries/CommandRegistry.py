from typing import List
from Commands.BaseCommand import Command
from Utils.Utils import find_executable_in_path
from Errors.CommandNotFound import CommandNotFound
from Commands.ExternalCommandWrapper import ExternalCommandWrapper

class CommandRegistry:
    _registry = {}

    @classmethod
    def register(cls, command_class: type[Command]):
        
        if not issubclass(command_class, Command):
            raise TypeError(f"Class {command_class.__name__} must be a subclass of Command.")

        cls._registry[command_class.__name__.lower()] = command_class
        return command_class

    @classmethod
    def list_commands(cls) -> List[str]:
        return list(cls._registry.keys())

    @classmethod
    def get_command(cls, command_name: str) -> Command:
        builtin_command_class = cls._registry.get(command_name.lower())

        if builtin_command_class:
            return builtin_command_class()
        else:
            executable_path = find_executable_in_path(command_name)

            if executable_path:
                return ExternalCommandWrapper(executable_path)
            else:
                raise CommandNotFound(command_name)

