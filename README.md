# AirBnB Clone - The Console

## Overview
This project is the first step towards building an AirBnB clone. The goal is to create a command-line interpreter that manages AirBnB objects, including creating new objects, retrieving objects, performing operations on objects, updating attributes, and destroying objects. The command interpreter will interact with objects of various classes like User, State, City, Place, etc.

## Project Structure
The project is organized into modules and tests. The main modules include:

- **base_model.py:** Defines the BaseModel class, which serves as the parent class for all other classes. Handles initialization, serialization, and deserialization.
- **user.py:** Defines the User class, which inherits from BaseModel.
- **state.py:** Defines the State class, which inherits from BaseModel.
- **city.py:** Defines the City class, which inherits from BaseModel.
- **place.py:** Defines the Place class, which inherits from BaseModel.
- **review.py:** Defines the Review class, which inherits from BaseModel.
- **amenity.py:** Defines the Amenity class, which inherits from BaseModel.
- **__init__.py:** Initializes the package.
- **console.py:** Implements the command-line interpreter using the cmd module.

## Usage
To run the command-line interpreter, execute the following command:

```bash
./console.py

## Command Interpreter
The command interpreter supports various commands for managing objects:

| Commands                  | Description                                                                       |
|---------------------------|-----------------------------------------------------------------------------------|
| `quit` or `Ctrl+D`        | Quits the console.                                                                |
| `help` or `help <command>`| Displays all commands or instructions for a specific command.                      |
| `create <class>`          | Creates an object of a specified class, saves it to a JSON file, and prints its ID.|
| `show <class> <ID>`       | Displays the string representation of an object.                                  |
| `destroy <class> <ID>`    | Deletes an object.                                                                |
| `all` or `all <class>`    | Prints string representations of all objects or objects of a specific class.      |
| `update <class> <ID> <attribute name> "<attribute value>"` | Updates an object with a certain attribute.
