import sys
from typing import List
from Commands.BaseCommand import Command
from Registries.CommandRegistry import CommandRegistry

@CommandRegistry.register
class Echo(Command):
    def execute(self, args: List[str]):
        string = " ".join(args)
        sys.stdout.write(string + "\n")
        return 0