class CommandNotFound(Exception):
    def __init__(self, command_name: str) -> None:
        self.command_name = command_name
        super().__init__(f"{command_name}: command not found")

    def __str__(self):
        return f"{self.command_name}: command not found"