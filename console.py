#!/usr/bin/python3
"""Entry point for the command interpreter """
import cmd
import re
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def parser(arg):
    """Remove commas and quatation"""

    for i in range(len(arg)):
        arg[i] = arg[i].strip('\",')

    return arg

class HBNBCommand(cmd.Cmd):
    """Command interpreter class for AirBnB program"""

    prompt = '(hbnb) '

    __classes = {"BaseModel", "User", "State",
                 "City", "Amenity", "Place", "Review"}

    def default(self, arg):
        """TBD"""
        method_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "update": self.do_update,
            "destroy": self.do_destroy,
            "count": self.do_count
        }

        match = re.search("\.", arg)
        if match is not None:
            input_list = [arg[:match.span()[0]], arg[match.span()[1]:]]
            input_list[1] = re.sub('[",]+', '', input_list[1])
            match = re.search("\((.*?)\)", input_list[1])

            if match is not None:
                cmd_list = [input_list[1][:match.span()[0]], match.group()[1:-1]]
                print("Cmd_list: {}".format(cmd_list))
                if cmd_list[0] in method_dict.keys():
                    arguments = input_list[0] + " " + cmd_list[1]
                    print("Arguments: {}".format(arguments))
                    return method_dict[cmd_list[0]](arguments)
        print("*** Unknown syntax: {}".format(arg))
        return False

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
        """Help output for the create command"""
        print("Creates a new instance of a class, saves it and prints the id")
        print()

    def do_show(self, arg):
        """
        Prints string representation of an instance based on class name and id
        """
        line = arg.split()
        line = parser(line)
        if len(line) == 0:
            print("** class name missing **")
        else:
            if not line[0] in self.__classes:
                print("** class doesn't exist **")
            elif len(line) == 1:
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

    def help_show(self):
        """Help output for the show command"""
        print("Prints string representation of an instance\
        based on class name and id")
        print()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based/not on the class name
        """
        line = arg.split()
        inst_list = []
        if len(line) == 0:
            for key, value in storage.all().items():
                inst_list.append(value.__str__())
            print(inst_list)
        elif not line[0] in self.__classes:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                cls_name = key.split(".")
                if cls_name[0] == line[0]:
                    inst_list.append(value.__str__())
            print(inst_list)

    def help_all(self):
        """Help output for the all command"""
        print("Prints all string representation of all instances\
        based/not on the class name")
        print()

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        line = arg.split()
        line = parser(line)
        if len(line) == 0:
            print("** class name missing **")
        else:
            if not line[0] in self.__classes:
                print("** class doesn't exist **")
            elif len(line) != 2:
                print("** instance id missing **")
            else:
                search_key = line[0] + "." + line[1]
                check = False
                for key, value in storage.all().items():
                    if search_key == key:
                        check = True
                        del storage.all()[key]
                        storage.save()
                        break
                if not check:
                    print("** no instance found **")

    def help_destroy(self):
        """Help output for the destroy command"""
        print("Deletes an instance based on the class name and id\
        (save the change into the JSON file)")
        print()

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file)
        """
        line = arg.split()
        line = parser(line)
        if len(line) == 0:
            print("** class name missing **")
        else:
            if not line[0] in self.__classes:
                print("** class doesn't exist **")
            elif len(line) == 1:
                print("** instance id missing **")
            else:
                check = False
                for key, value in storage.all().items():
                    id_no = key.split(".")
                    if id_no[1] == line[1]:
                        check = True
                        if len(line) == 2:
                            print("** attribute name missing **")
                        elif len(line) == 3:
                            print("** value missing **")
                        else:
                            if line[3].isalpha():
                                pass
                            elif line[3].isdigit():
                                line[3] = int(line[3])
                            else:
                                line[3] = float(line[3])
                            setattr(value, line[2], line[3])
                            storage.save()
                if not check:
                    print("** no instance found **")

    def help_update(self):
        """Help output for the update command"""
        print("Updates an instance based on the class name and id by\
        adding or updating attribute (save the change into the JSON file)")
        print()

    def do_count(self, arg):
        """Count number of instances of a class"""
        count = 0
        line = arg.split()
        if len(line) == 0:
            print("** class name missing **")
        else:
            if not line[0] in self.__classes:
                print("** class doesn't exist **")
            else:
                for key in storage.all().keys():
                    cls_name = key.split(".")
                    if cls_name[0] == line[0]:
                        count += 1
                print(count)

    def help_count(self):
        """Help output for the update command"""
        print("Counts the number of instances of a class")
        print()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
