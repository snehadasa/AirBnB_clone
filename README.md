**AirBnB clone - The Console**

![hbnb Logo](https://imgur.com/OilEsXV.png "hbnb logo")

**Overview**

This is the first step towards building the full web application: the AirBnB clone. This is a part of The Holberton School Full Stack Software Enginnering Program. This part consists of a command-line interpreter for data management and a database or files that store data.The main goal of the project is to deploy a simple copy of the AirBnB website.

**What’s a command interpreter?**

1. Create a new object
2. Retrieve an object from a file, a database
3. Do operations on objects
4. Update attributes of an object
5. Destroy an object

**Usage**

1. The console works in both interactive and non-interactive modes.
2. Controls the website with the application.

**Features**

Like the Unix-Shell shell, the console handles command line inputs along with arguments.
Some of the following are,

| No. | command | Description |
| --- | ------- | ----------- |
| 1. | Quit | Quits the console | (hbnb) quit |
| 2. | Help | Displays the help for particular commands | (hbnb) help |
| 3. | Create | creates an object | (hbnb) create <class> |
| 3. | Show | show an object | (hbnb) show <class> <id> |
| 3. | Destroy | destroys an object | (hbnb) destroy <class> <id> |
| 3. | All | shows all objects | (hbnb) all <class> <id> |
| 3. | Update | updates an attribute with an object | (hbnb) create <class> <id> <attribute name> "<attribute value>"|
| 3. | Run | run the console | ./console.py |

**examples**

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit


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


**About**

All files were created and compiled on Ubuntu 14.04.4 LTS using python3 (version 3.4.3)

**Files**

| Files | Description |
| ----- | ----------- |
| base_model.py | BaseModel defines all common attributes/methods for other classes |
| file_storage.py | serializes instances to a JSON file and deserializes JSON file to instances |
| __init__.py | create instance for application |
| console.py | entry point of the command interpreter |
| user.py | User class for user info which inherits from superclass BaseModel |
| state.py | State class for state info which inherits from superclass BaseModel |
| city.py | City class for city info which inherits from superclass BaseModel |
| amenity.py | Amenity class for amenity info which inherits from superclass BaseModel |
| place.py | Place class for place info which inherits from superclass BaseModel |
| review.py | Review class for review info which inherits from superclass BaseModel |

**Tests**

All the code are tested using Unittest Module.The unittest module provides a rich set of tools for constructing and running tests.

**Authors**

**Van Duy Phan** - @Van_D_Phan
**Sneha Dasa Lakshminath** - @DasaSneha
