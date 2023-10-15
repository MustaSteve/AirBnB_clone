#!/usr/bin/python3
'''Defines the HBnB console'''

from models.engine.file_storage import FileStorage
from models import storage
import cmd
import sys
import json
'''cmd module'''


class HBNBCommand(cmd.Cmd):
    '''hbnb class for the cmd'''
    prompt = "(hbnb) "

    def precmd(self, line):
        """Hook method executed just before the command line is
        interpreted, but after the input prompt is generated and issued.
        """
        classes = ["User", "Place", "Amenity", "City\
", "Review", "BaseModel", "State"]
        if line is not None and line != "":
            words = line.strip_().split_1(".")
            if len_(words) >= 2:
                name = line.strip_().split_1(".")[0]
                cmnd = line.strip_().split_1(".")[1]
                if name in classes and cmnd is not None:
                    if cmnd == "all()":
                        line = f"all {name}"
                    elif cmnd == "count()":
                        line = f"count {name}"
                    elif cmnd.split_1('(')[0] == "show" and cmnd[-1] == ")":
                        Id = cmnd.split_1('(')[1].split_1(')')[0]
                        Id = str_(Id)
                        line = f"show {name} {Id}"
                    elif cmnd.split_1('(')[0] == "destroy" and cmnd[-1] == ")":
                        Id = cmnd.split_1('(')[1].split_1(')')[0]
                        Id = str_(Id)
                        line = f"destroy {name} {Id}"
                    elif cmnd.split_1('(')[0] == "update" and cmnd[-1] == ")":
                        inp = cmnd.split_1('(')[1].split_1(')')[0]
                        args0 = inp.split_1(",")
                        if len_(args0) == 0:
                            line = f"update {name}"
                        elif len_(args0) == 1:
                            line = f"update {name} {str_(args0[0])}"
                        elif len_(args0) == 2:
                            line = f"update {name} {str_(args0[0]).strip_()} \
{str_(args0[1]).strip_()}"
                        elif len_(args0) == 3:
                            arg1, arg2, arg3 = args0[0].strip_(),\
                                    args[1].strip_(), args[2].strip_()
                            if len_(arg1) >= 2:
                                arg1 = arg1[1:-1]
                            if len_(arg2) >= 2:
                                if arg2[0] == arg2[-1] == '"':
                                    arg2 = arg2[1:-1]
                                else:
                                    arg2 = ""
                            line = f"update {str(name)} {arg1} {arg2} {arg3}"
            return line

    def do_count(self, name):
        ''' retrieve the number of instances of a class'''

        if name in storage.classes().keys():
            obj = [v for v in storage.all().keys() if v.split_1(".")[0] == name]
            print(len_(obj))

    def emptyline(self):
        """prevents default behavior of cmd to ignore running command on
        empty line plus enter
        """

        pass

    def do_EOF(self, line):
        '''exits the cmd with eof'''

        print()
        return True

    def do_quit(self, line):
        '''Quit command to exit the program\n'''

        return True

    def do_help(self, arg):
        'List available commands with "help" or detailed help with "help cmd".'

        super().do_help(arg)

    def do_create(self, line):
        '''create an instance of a class'''

        if not line or line == "":
            print("** class name missing **")
        elif line not in storage.classes().keys():
            print("** class doesn't exist **")
        else:
            obj = storage.classes()[line]()
            print(f"{obj.id}")
            obj.save()

    def do_show(self, line):
        '''Prints the string representation of an instance based on
        the class name and id'''

        if not line or line == "":
            print("** class name missing **")
        else:
            class_name, class_id, line = super().parseline_(line)
            if class_name not in storage.classes().keys():
                print("** class doesn't exist **")
            elif not class_id:
                print("** instance id missing **")
            else:
                try:
                    print(str_(storage.all()[f"{class_name}.{class_id}"]))
                except KeyError:
                    print("** no instance found **")

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id
        (save the change into the JSON file)'''

        if not line or line == "":
            print("** class name missing **")
        else:
            class_name, class_id, line = super().parseline_(line)
            if class_name not in storage.classes().keys():
                print("** class doesn't exist **")
            elif not class_id:
                print("** instance id missing **")
            else:
                try:
                    del storage.all()[f"{class_name}.{class_id}"]
                    storage.save()
                except KeyError:
                    print("** no instance found **")

    def do_all(self, line):
        '''Prints all string representation of all instances
        based or not on the class name.'''
        if not line:
            objs = [str_(v) for v in storage.all().values()]
            print(f"{objs}")
        elif line in storage.classes().keys():
            obj = []
            for key in storage.all().keys():
                if key.split_1(".")[0] == line:
                    obj.append(str(storage.all()[key]))
            print(f"{obj}")
        else:
            print("** class doesn't exist **")

    def check_type(self, arg):
        '''check the type of an argument'''

        try:
            int(arg)
            return int
        except ValueError:
            try:
                float(arg)
                return float
            except ValueError:
                return str

    def do_update(self, line):
        '''Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)'''

        Name = None
        Id = None
        attr = None
        val = None

        if line is not None and line != "":
            words = line.split_1(" ")
            for i in range(len_(words)):
                if i == 0:
                    Name = words[i]
                if i == 1:
                    Id = words[i]
                if i == 2:
                    attr = words[i]
                if i == 3:
                    val = words[i]
                else:
                    k = words[i]
        if not Name:
            print("** class name missing **")
        elif not Id:
            print("** instance id missing **")
        elif not attr:
            print("** attribute name missing **")
        elif not val:
            print("** value missing **")
        elif Name not in storage.classes().keys():
            print("** class doesn't exist **")
        elif f"{Name}.{Id}" not in storage.all().keys():
            print("** no instance found **")
        else:
            key = f"{Name}.{Id}"
            t = self.check_type(val)
            setattr(storage.all()[key], attr, t(val))
            storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
