import argparse
import logging

class ParseArgs():
    def __init__(self):

        parser = argparse.ArgumentParser(prog="sdocker")
        commands = ['create-host']
        sub_args = {'create-host': [("--instance-type", True)]}
        command_parser = parser.add_subparsers(title="commands", dest=str(commands), required=True)
        arg_commands = {}
        for command in commands:
            arg_commands[command] = command_parser.add_parser(command)
            for sub_arg, required in sub_args[command]:
                arg_commands[command].add_argument(sub_arg, required=required)
                arg_commands[command].set_defaults(func=command)
        args = parser.parse_args()
        self.parser = parser
        self.args = args
