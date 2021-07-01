## <img src="https://i.ibb.co/2NBYbYv/CLON1.png">

# Project: AirBnB clone - The Console

_This project consists of making a clone of the original page <a target="_blank" href="https://www.airbnb.com/">AirBnB Clone</a>, in this folder we create a console Where we will manage and manipulate the JSON file where the information of the Basemodel object will be handled._

# Console

_You can use the console in two mode in an **interactive** mode and **non-interactive** mode._

- See the examples.

### Interactive mode.

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
```

### Non-interactive mode.

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

### Storage

The storage and handling of the JSON file will be done through `file.json` on which it contains the information and management of the created objects.

### Use of the console. 📖

- Start or enter the console You must run the `console.py` file in this way.

_This is going to give way to the option in which you are going to use the interactive mode of the console._

### Interactive.

```console
./console.py
(hbnb)
```

### **Basic Commands**

> Command: `help` This command will provide you basic console information or a specific covenant as well `help <command>`.

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
all     destroy  quit  update  EOF
create  help     show

(hbnb) help create
Usage: create <valid class name>
```

> Command: `quit`, `EOF` or `ctrl + d` Is the Same, this Commands will end up financed to the console.

```bash
$ ./console.py
(hbnb) quit
$
$ ./console.py
(hbnb) EOF
$
$ ./console.py
(hbnb) <ctrl + d>
$
```

### **Manipulation Commands**

> Command: `create` this command creates a new instance of the specified class, printing the unique ID of the class.

#### Usage:

- `create <valid class name>`

```bash
$./console.py
(hbnb) create BaseModel
c3461d51-59c4-4603-857d-97f1cf356e4b <- ID of the instance
(hbnb) quit
$cat file.json | tr ',' '\n'
{"BaseModel.c3461d51-59c4-4603-857d-97f1cf356e4b": {"id": "c3461d51-59c4-4603-857d-97f1cf356e4b"
"created_at": "2021-07-01T13:48:38.177105"
"updated_at": "2021-07-01T13:48:38.177214"
"__class__": "BaseModel"}}
```

> Command: `show` This command shows you the information of a previously created instance.

#### Usage:

- `show <valid class name> <valid id>`
- `<valid class name>.show(<valid id>)`

```bash
$./console.py
(hbnb) show BaseModel c3461d51-59c4-4603-857d-97f1cf356e4b
[BaseModel] (c3461d51-59c4-4603-857d-97f1cf356e4b) {'id': 'c3461d51-59c4-4603-857d-97f1cf356e4b', 'created_at': datetime.datetime(2021, 7, 1, 13, 48, 38, 177105), 'updated_at': datetime.datetime(2021, 7, 1, 13, 48, 38, 177214)}
(hbnb)
```

> Command: `destroy` This command deletes a storage class in the file `file.json`.

- `destroy <valid class name> <valid id>`
- `<valid class name>.destroy(<valid id>)`

```bash
$./console.py
(hbnb) create User
926827af-f08b-4489-b9a9-d175690bb5f0
(hbnb) destroy User 926827af-f08b-4489-b9a9-d175690bb5f0
(hbnb) show User 926827af-f08b-4489-b9a9-d175690bb5f0
** no instance found **
(hbnb)
```

> Commmand: `all` This command prints the information of all previously created classes instances.

#### Usage:

- `all `
- `all <valid class name>`
- `<valid class name>.all()`

```bash
$./console.py
(hbnb) all User
["[User] (607ca8cb-fd72-4586-aebf-6df0d31047ec) {'id': '607ca8cb-fd72-4586-aebf-6df0d31047ec', 'created_at': datetime.datetime(2021, 7, 1, 14, 5, 32, 896332), 'updated_at': datetime.datetime(2021, 7, 1, 14, 5, 32, 896394)}", "[User] (b28d99ec-fc8c-4ed2-9c55-4741088bd0e1) {'id': 'b28d99ec-fc8c-4ed2-9c55-4741088bd0e1', 'created_at': datetime.datetime(2021, 7, 1, 14, 9, 42, 515846), 'updated_at': datetime.datetime(2021, 7, 1, 14, 9, 42, 515954)}"]
(hbnb)
```

> Command: `update` Updates a class instance based on a given id with a given key/value attribute pair or dictionary of attribute pairs

#### Usage:

- `update <class> <id> <attribute name> "<attribute value>"`
- `<class>.update(<id>, <attribute name>, <attribute value>)`
- `<class>.update(<id>, <attribute dictionary>)`

```bash
$./console.py
(hbnb) create User
47bcf711-4bc6-4bb5-950c-458488fb3dfb
(hbnb) show User 47bcf711-4bc6-4bb5-950c-458488fb3dfb
[User] (47bcf711-4bc6-4bb5-950c-458488fb3dfb) {'id': '47bcf711-4bc6-4bb5-950c-458488fb3dfb', 'created_at': datetime.datetime(2021, 7, 1, 14, 47, 42, 701823), 'updated_at': datetime.datetime(2021, 7, 1, 14, 47, 42, 701922)}
(hbnb) update User 47bcf711-4bc6-4bb5-950c-458488fb3dfb first_name "Betty"
(hbnb) show User 47bcf711-4bc6-4bb5-950c-458488fb3dfb
[User] (47bcf711-4bc6-4bb5-950c-458488fb3dfb) {'id': '47bcf711-4bc6-4bb5-950c-458488fb3dfb', 'created_at': datetime.datetime(2021, 7, 1, 14, 47, 42, 701823), 'updated_at': datetime.datetime(2021, 7, 1, 14, 47, 42, 701922), 'first_name': 'Betty'}
```

> Commmand: `count` This command prints the number of instances of the class.

#### Usage:

- `<valid class name>.count()`

```bash
$./console.py
(hbnb) User.count()
0
(hbnb)
```

### Testing 🤖

_To run the entire test suite simultaneously, execute the following commands_:

```bash
$ python3 unittest -m discover tests
```

> Testing a specify test:

```bash
$ python3 unittest -m tests/test_console.py
```

### 🗃 - Folders and files

| Folders            | Description                             |
| ------------------ | :-------------------------------------- |
| [models](./models) | Folders with models to handler.         |
| [tests](./tests)   | Folders with test of models and engine. |

| Files                      | Description                                      |
| -------------------------- | :----------------------------------------------- |
| [console.py](./console.py) | Logic of shell in Python interpret the commands. |
| [tests](./tests)           | Folders with test of models and engine.          |

### Authors. <img src="https://image.flaticon.com/icons/png/512/25/25231.png" width="25" height="25">

- _Samuel Trujillo_ : [@samutrujillo](https://github.com/samutrujillo)
- _Sergio Ramos_ : [@Sergioarg](https://github.com/Sergioarg)
