import sys
from typing import List
from Commands.BaseCommand import Command
from Utils.Utils import find_executable_in_path
from Registries.CommandRegistry import CommandRegistry

@CommandRegistry.register
class Type(Command):
    def execute(self, args: List[str]):
        if not args:
            sys.stderr.write("type: missing operand\n")
            return 1

        command_name_to_check = args[0] 

        if CommandRegistry._registry.get(command_name_to_check.lower()):
            sys.stdout.write(f"{command_name_to_check} is a shell builtin\n")
            return 0

        executable_path = find_executable_in_path(command_name_to_check)

        if executable_path:
            sys.stdout.write(f"{command_name_to_check} is {executable_path}\n")
            return 0
        else:
            sys.stdout.write(f"{command_name_to_check}: not found\n")
            return 1