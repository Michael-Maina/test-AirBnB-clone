#!/usr/bin/python3
"""Entry point for the command interpreter """
import cmd
import json
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for AirBnB program"""

    prompt = '(hbnb) '

    __classes = {"BaseModel", "User", "State",
                 "City", "Amenity", "Place", "Review"}

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

    def do_create(self, arg):
        """
        Creates a new instance of a class, saves it and prints the id
        """
        line = arg.split()
        if len(line) == 0:
            print("** class name missing **")
        else:
            if not line[0] in self.__classes:
                print("** class doesn't exist **")
            else:
                new_inst = eval(line[0])()
                new_inst.save()
                print("{}".format(new_inst.id))

    def help_create(self):
        """Help output for create command"""
        print("Creates a new instance of a class, saves it and prints the id")
        print()

    def do_show(self, arg):
        """
        Prints string representation of an instance based on class name and id
        """
        line = arg.split()
        if len(line) == 0:
            print("** class name missing **")
        else:
            if not line[0] in self.__classes:
                print("** class doesn't exist **")
            elif line[1] == "":
                print("** instance id missing **")
            else:
                search_key = line[0] + "." + line[1]
                check = False
                for key, value in storage.all().items():
                    if search_key == key:
                        check = True
                        print(value)
                        break
                if not check:
                    print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based/not on the class name
        """
        line = arg.split()
        if len(line) == 0:
            for key, value in storage.all().items():
                print(value)
        elif not line[0] in self.__classes:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                cls_name = key.split(".")
                if cls_name[0] == line[0]:
                    print(value)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        line = arg.split()
        if len(line) == 0:
            print("** class name missing **")
        else:
            if not line[0] in self.__classes:
                print("** class doesn't exist **")
            elif line[1] == "":
                print("** instance id missing **")
            else:
                search_key = line[0] + "." + line[1]
                check = False
                for key, value in storage.all().items():
                    if search_key == key:
                        check = True
                        del storage.all()[key]
                        break
                if not check:
                    print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
