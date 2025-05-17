import sys
from typing import List
from Commands.BaseCommand import Command
from Registries.CommandRegistry import CommandRegistry

@CommandRegistry.register
class ListCommands(Command):
    def execute(self, args: List[str]):
        commands = CommandRegistry.list_commands()
        sys.stdout.write("Available builtins:\n")
        for cmd in commands:
            sys.stdout.write(f"- {cmd}\n")
        return 0