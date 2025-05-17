import os
import sys
from typing import List
from Commands.BaseCommand import Command
from Registries.CommandRegistry import CommandRegistry

@CommandRegistry.register
class Pwd(Command):
    def execute(self, args: List[str]) -> int | None:
        pwd = os.getcwd()
        sys.stdout.write(f"{pwd}\n")
        return 0