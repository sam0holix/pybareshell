import sys
import shlex
from Errors.ExitStatus import ExitStatus
from Errors.CommandNotFound import CommandNotFound
from Registries.CommandRegistry import CommandRegistry
from Commands import load_all_builtins


def main():
    exit_code = 0
    load_all_builtins()
    while True:
        try:
            sys.stdout.write("$ ")
            line = input().strip()

            if not line:
                continue

            parts = shlex.split(line)
            command_name = parts[0]
            args = parts[1:]

            command_object = CommandRegistry.get_command(command_name)

            command_exit_code = command_object.execute(args)

            if command_name.lower() != 'exit':
                exit_code = command_exit_code


        except ExitStatus as e:
            exit_code = e.args[0] if e.args else 0
            break
        except CommandNotFound as e:
            print(e)
            exit_code = 127
        except KeyboardInterrupt:
            exit_code = 0
            print("\nExiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            exit_code = 1

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
