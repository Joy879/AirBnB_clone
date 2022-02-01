# The Console: 0x00. AirBnB clone

![65f4a1dd9c51265f49d0](https://user-images.githubusercontent.com/70502261/151993984-204d5d84-c703-434d-a23f-8855a7c6fdb2.png)


### Description

This repository contains the first steps of the AirBnB clone project made for Holberton/ALX_Africa students. During this first part of the project we had to:

* Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances.
* Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* Create the first abstracted storage engine of the project: File storage.
* Create all unittests to validate all our classes and storage engine
* Create a command interpreter that can:
>	- create a new object (eg. a new User or a new Place)
>	- retrieve an object from a file
>	- update attributes of an object
>	- destroy an object



### Files and directories description

| Directory | Description |
|--|--|
| Models | contains all the classes used (eg. `BaseModel`, `User`, `City`, etc.)
| Models/Engine | contains the file `file_storage.py` that holds class `FileStorage`
| Tests | contains all unit tests

---------------------

### Usage

The following is how the interpreter works in interactive mode.

`help`: displays the commands the interpreter can use

```
~/AirBnB_clone$ ./console.py
(hbnb)
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
```

It should work like this in non-interactive mode.

```bash
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
$
```

`create`: creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the `id`

```
(hbnb) create BaseModel
79ee3ea4-3851-4ceb-bf88-8bc535190ee4  # BaseModel id number
```

`show`: prints the string representation of an instance based on the class name and `id`
`update`: updates an instance based on the class name and `id` by adding or updating attribute (saves the change into the JSON file)

```
(hbnb) show BaseModel 79ee3ea4-3851-4ceb-bf88-8bc535190ee4
[BaseModel] (79ee3ea4-3851-4ceb-bf88-8bc535190ee4) {'id': '79ee3ea4-3851-4ceb-bf88-8bc535190ee4', 'created_at': datetime.datetime(2020, 2, 18, 23, 34, 49, 766357), 'updated_at': datetime.datetime(2020, 2, 18, 23, 34, 49, 766389)}
(hbnb)
(hbnb) update BaseModel 79ee3ea4-3851-4ceb-bf88-8bc535190ee4 first_name "Betty"
(hbnb)
(hbnb) show BaseModel 79ee3ea4-3851-4ceb-bf88-8bc535190ee4
[BaseModel] (79ee3ea4-3851-4ceb-bf88-8bc535190ee4) {'first_name': 'Betty', 'updated_at': datetime.datetime(2020, 2, 18, 23, 34, 49, 766389), 'id': '79ee3ea4-3851-4ceb-bf88-8bc535190ee4', 'created_at': datetime.datetime(2020, 2, 18, 23, 34, 49, 766357)}
```

`destroy`: deletes an instance based on the class name and `id`

```
(hbnb) destroy BaseModel 79ee3ea4-3851-4ceb-bf88-8bc535190ee4
(hbnb)
(hbnb) show BaseModel 79ee3ea4-3851-4ceb-bf88-8bc535190ee4
** no instance found **
```

`quit`: command to exit the interpreter

```
(hbnb) exit
*** Unknown syntax: exit
(hbnb)
(hbnb) quit
~/AirBnb_clone$  # successfully exited the interpreter
```

## Authors

[Benroy Kirwa](https://github.com/BenroyKirwa)

[Joy Wanjiru](http://github.com/Joy879)
