#!/usr/bin/python3
"""The Airbnb console"""

import cmd
import shlex
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "Place": Place,
           "Review": Review, "State": State, "User": User, "City": City}


class HBNBCommand(cmd.Cmd):
    """"principal class"""

    prompt = "(hbnb) "

    def do_quit(self, inp):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, inp):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """blanks when you press ENTER"""
        pass

    def do_create(self, inp):
        """ create an new instance """
        try:
            arguments = inp.split()
            if len(arguments) == 0:
                print("** class name missing **")
                return False
            if arguments[0] in classes:
                object = classes[arguments[0]]()
            else:
                print("** class doesn't exist **")
                return False
            print(object.id)
            object.save()
        except Exception:
            raise

    def do_show(self, argum):
        """show class"""
        models.storage.reload()
        if len(argum) == 0:
            print("** class name missing **")
            return
        argum_list = argum.split()
        try:
            instance = eval(argum_list[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(argum_list) == 1:
            print("** instance id missing **")
            return
        elif len(argum_list) > 1:
            key = argum_list[0] + "." + argum_list[1]
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")
                return

    def do_destroy(self, argum):
        """ Destroy  instance of class id """
        if len(argum) == 0:
            print("** class name missing **")
            return
        argum_list = argum.split()
        try:
            instance = eval(argum_list[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(argum_list) == 1:
            print("** instance id missing **")
            return
        elif len(argum_list) > 1:
            key = argum_list[0] + "." + argum_list[1]
            if key in models.storage.all():
                models.storage.all().pop(key)
                models.storage.save()
            else:
                print("** no instance found **")
                return

    def do_all(self, argum):
        """Display all instances based on class name"""
        models.storage.reload()
        if len(argum) < 1:
            new_list = []
            for value in models.storage.all().values():
                new_list.append(str(value))
            if not new_list:
                return
            print(new_list)
        else:
            modelClass = argum.split(" ")
            if modelClass[0] not in classes:
                print("** class doesn't exist **")
            elif modelClass[0] in classes:
                new_list = []
                for value in models.storage.all().values():
                    if modelClass[0] in value.__class__.__name__:
                        new_list.append(str(value))
                if not new_list:
                    return
                print(new_list)

    def do_update(self, argum):
        """ update an instance based on its UUID """
        models.storage.reload()
        if len(argum) == 0:
            print("** class name missing **")
            return
        else:
            ac = shlex.split(argum)
            if ac[0] not in classes:
                print("** class doesn't exist **")
                return
            if ac[0] in classes and len(ac) < 2:
                print("** instance id missing **")
                return
            tmp = ac[0] + '.' + ac[1]
            if tmp in models.storage.all():
                to_update = models.storage.all()[tmp].__dict__
                if len(ac) < 3:
                    print("** attribute name missing **")
                elif len(ac) < 4:
                    print("** value missing **")
                else:
                    key = ac[2]
                    try:
                        attr = type(to_update[key])
                        value = attr(ac[3])
                    except KeyError:
                        value = ac[3]
                    to_update[key] = value
                    models.storage.save()
            else:
                print("** no instance found **")

    def count(self, arg):
        """Count instances"""
        count = 0
        arg_list = arg.split(' ')
        for key in models.storage.all():
            obj_class = models.storage.all()[key]
            if arg_list[0] == obj_class.__class__.__name__:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
