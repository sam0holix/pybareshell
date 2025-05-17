import sys
import subprocess
from typing import List
from Commands.BaseCommand import Command

class ExternalCommandWrapper(Command):
    def __init__(self, executable_path: str):
        
        self.executable_path = executable_path.split('/').pop()

    def execute(self, args: List[str]): 
        try:
            process = subprocess.run([self.executable_path] + args, capture_output=True, text=True)

            sys.stdout.write(process.stdout)
            sys.stderr.write(process.stderr)

            return process.returncode
        except FileNotFoundError:
            sys.stderr.write(f"{self.executable_path}: command not found\n")
        except Exception as e:
            sys.stderr.write(f"Error executing {self.executable_path}: {e}\n")
            return 1 
