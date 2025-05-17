import os
import sys
from typing import List
from Commands.BaseCommand import Command
from Registries.CommandRegistry import CommandRegistry

@CommandRegistry.register
class Cd(Command):
    def execute(self, args: List[str]) -> int | None:
            path = os.path.join(args[0])
            if args[0] == "~":
                path = os.environ.get('HOME', '')
            if os.path.exists(path):
                os.chdir(path)
                return 0
            sys.stdout.write(f"cd: {path}: No such file or directory\n")