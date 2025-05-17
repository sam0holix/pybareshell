import sys
from typing import List
from Commands.BaseCommand import Command
from Errors.ExitStatus import ExitStatus
from Registries.CommandRegistry import CommandRegistry

@CommandRegistry.register
class Exit(Command):
    def execute(self, args: List[str]):
        exit_code = 0 

        if args:
            try:
                exit_code = int(args[0])
            except ValueError:
                sys.stderr.write(f"exit: {args[0]}: numeric argument required\n")
                exit_code = 2
            except IndexError:
                pass

        raise ExitStatus(exit_code)