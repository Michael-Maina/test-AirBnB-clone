#!/usr/bin/python3
"""Entry point for the command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for AirBnB program"""

    prompt = '(hbnb) '

    def do_emptyline(self):
        """Executes nothing when no command is passed to the interpreter"""
        pass

    def do_EOF(self, arg):
        """EOF(end_of_file) command to exit the interpreter"""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the interpreter"""
        return True

    def do_petty(self, arg):
        """testing input processing"""
        line = arg.split()
        print("1. {} and 2. {}".format(line[0], line[1]))

    def help_petty(self):
        """Help output for petty command"""
        print("This command is meant to test out a few examples")
        print()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
