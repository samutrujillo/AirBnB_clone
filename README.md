## <img src="https://i.ibb.co/2NBYbYv/CLON1.png">

# Project: AirBnB clone - The Console

_This project consists of making a clone of the original page <a href="https://www.airbnb.com/">AirBnB Clone</a>, in this folder we create a console Where we will manage and manipulate the JSON file where the information of the Basemodel object will be handled._

# Console

_You can use the console in two mode in an **interactive** mode and **non-interactive** mode._

- See the examples.

### Interactive.

```Python
    $ ./console.py
    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit

    (hbnb)
    (hbnb)
    (hbnb) quit
    $
```

### Non-interactive mode.

```Python
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

### Use of the console.

**Commands**

- all
- show
- create
- destroy

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
