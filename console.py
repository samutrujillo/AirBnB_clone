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
        """[Count instances of a Class.]"""
        count = 0
        arg_list = arg.split(' ')
        for key in models.storage.all():
            obj_class = models.storage.all()[key]
            if arg_list[0] == obj_class.__class__.__name__:
                count += 1
        print(count)

    ##################
    # Help Functions #
    ##################

    def help_quit(self):
        """[shows command help]"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """ [shows command help]"""
        print("CTRL + D (EOF) to exit the program")

    def help_create(self):
        """[show help for create command]"""
        print("Usage: create <valid class name>")

    def help_show(self):
        """[show help for show command]"""
        print("Usage: show <valid class name> <valid id>")

    def help_destroy(self):
        """[show help for destroy command]"""
        print("Usage: destroy <valid class name> <valid id>")

    def help_all(self):
        """[show help for all command]"""
        print("Usage: all OR all <valid class name>")

    def help_update(self):
        """[show help for update update command]"""
        print("Usage: update <valid class name>", end="")
        print("<valid id> <attribute name> <attribute value>")

    ##########
    # call all function
    #########

    def do_User(self, args):
        """[Usages:
        User.all() - displays all objects of class User
        User.count() - displays number of objects of class User
        User.show(<id>) - displays object of class User with id
        User.destroy(<id>) - deletes object of class User with id
        User.update(id, attribute name, attribute value) - update User
        User.update(<id>, <dictionary representation>) - update User]
        """
        self.class_exec('User', args)

    def do_BaseModel(self, args):
        """[Usages:
        BaseModel.all() - displays all objects of class BaseModel
        BaseModel.count() - displays number of objects of class BaseModel
        BaseModel.show(<id>) - displays object of class BaseModel with id
        BaseModel.destroy(<id>) - deletes object of class BaseModel with id
        BaseModel.update(id, attribute name, attribute value) - update
        BaseModel.update(<id>, <dictionary representation>) - update]
        """
        self.class_exec('BaseModel', args)

    def do_State(self, args):
        """[Usages:
        State.all() - displays all objects of class State
        State.count() - displays number of objects of class State
        State.show(<id>) - displays object of class State with id
        State.destroy(<id>) - deletes object of class BaseModel with id
        State.update(<id>, <attribute name>, <attribute value>) - update
        State.update(<id>, <dictionary representation>) - update]
        """
        self.class_exec('State', args)

    def do_City(self, args):
        """[Usages:
        City.all() - displays all objects of class City
        City.count() - displays number of objects of class City
        City.show(<id>) - displays object of class City with id
        City.destroy(<id>) - deletes object of class City with id
        City.update(<id>, <attribute name>, <attribute value>) - update
        City.update(<id>, <dictionary representation>) - update]
        """
        self.class_exec('City', args)

    def do_Amenity(self, args):
        """[Usages:
        Amenity.all() - displays all objects of class Amenity
        Amenity.count() - displays number of objects of class Amenity
        Amenity.show(<id>) - displays object of class Amenity with id
        Amenity.destroy(<id>) - deletes object of class Amenity with id
        Amenity.update(<id>, <attribute name>, <attribute value>) - update
        Amenity.update(<id>, <dictionary representation>) - update]
        """
        self.class_exec('Amenity', args)

    def do_Place(self, args):
        """[Usages:
        Place.all() - displays all objects of class Place
        Place.count() - displays number of objects of class Place
        Place.show(<id>) - displays object of class Place with id
        Place.destroy(<id>) - deletes object of class Place with id
        Place.update(<id>, <attribute name>, <attribute value>) - update
        Place.update(<id>, <dictionary representation>) - update]
        """
        self.class_exec('Place', args)

    def do_Review(self, args):
        """[Usages:
        Review.all() - displays all objects of class Review
        Review.count() - displays number of objects of class Review
        Review.show(<id>) - displays object of class Review with id
        Review.destroy(<id>) - deletes object of class Review with id
        Review.update(<id>, <attribute name>, <attribute value>) - update
        Review.update(<id>, <dictionary representation>) - update]
        """
        self.class_exec('Review', args)

    def class_exec(self, cls_name, args):
        """[Wrapper function for <class name>.action()]"""
        if args[: 6] == '.all()':
            self.do_all(cls_name)
        elif args[: 7] == '.count(':
            self.count(cls_name)
        elif args[: 6] == '.show(':
            self.do_show(cls_name + ' ' + args[7: -2])
        elif args[: 9] == '.destroy(':
            self.do_destroy(cls_name + ' ' + args[10: -2])
        elif args[: 8] == '.update(':
            if '{' in args and '}' in args:
                new_arg = args[8: -1].split('{')
                new_arg[1] = '{' + new_arg[1]
            else:
                new_arg = args[8: -1].split(',')
            if len(new_arg) == 3:
                new_arg = " ".join(new_arg)
                new_arg = new_arg.replace("\"", "")
                new_arg = new_arg.replace("  ", " ")
                self.do_update(cls_name + ' ' + new_arg)
            elif len(new_arg) == 2:
                try:
                    dict = eval(new_arg[1])
                except:
                    return
                for j in dict.keys():
                    self.do_update(cls_name + ' ' +
                                   new_arg[0][1:-3] + ' ' +
                                   str(j) + ' ' + str(dict[j]))
            else:
                return
        else:
            print("Not a valid command")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
