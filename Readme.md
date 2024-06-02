# Fixed Width to CSV Parser

The objective of this project is to build a parser that reads from a **fixed width file** and outputs it to **csv file format**.

## Table of Contents

- [Fixed Width to CSV Parser](#fixed-width-to-csv-parser)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Windows](#windows)
    - [Linux and MacOS](#linux-and-macos)
  - [Code Structure](#code-structure)
    - [Philosophy](#philosophy)
    - [Files and Folders](#files-and-folders)
  - [Running the application](#running-the-application)
    - [Prerequisits](#prerequisits)
    - [Run the code](#run-the-code)
    - [Checking the output](#checking-the-output)
  - [Running the Tests](#running-the-tests)
    - [Prerequisits](#prerequisits-1)
    - [Running All Tests](#running-all-tests)
    - [Runnint Unit Tests](#runnint-unit-tests)
    - [Running Integration Tests](#running-integration-tests)
  - [Running in Docker](#running-in-docker)
    - [Prerequisits](#prerequisits-2)
    - [Build the container](#build-the-container)
    - [Starting the image](#starting-the-image)
    - [Running the applications and tests](#running-the-applications-and-tests)

## Installation

The following are in prerequisites
* Python (v 11 and above) is installed
* PYTHONPATH is configured to point to current folder

### Windows
1. Clone the repository:<br>
   Go to the base folder where you need to project installed
   ```bash
   git clone https://github.com/amitwats/fixed_width_to_csv.git
   ```
2. Switch to the project directory:
   ```bash
   cd fixed_width_to_csv
   ```
3. Create a virtual environment, activate it and install requirements into it:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   py -m pip install -r requirements.txt
   ```
### Linux and MacOS
1. Clone the repository:<br>
   Go to the base folder where you need to project installed
   ```bash
   git clone https://github.com/amitwats/fixed_width_to_csv.git
2. Switch to the project directory:
   ```bash
   cd fixed_width_to_csv
   ```
3. Create a virtual environment, activate it and install requirements into it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Code Structure

   ```bash
   fixed_width_to_csv/
   ├── configs/
   │ ├── specs.json
   │ └── config.py
   ├── input/
   ├── output/
   ├── parser/
   │ └── fw_2_csv_parser.py
   ├── tests/
   │ ├── data/
   │ ├── integration_tests/
   │ └── unit_tests/
   ├── .gitignore
   ├── main.py
   ├── .dockerignore
   ├── Dockerfile
   ├── README.md
   └── requirements.txt
   ```
### Philosophy
The code structure is designed to be extendable to become the base of a larger project. The code is written to be scalable for large input files.

### Files and Folders
* **main.py** :This is the starting point of where the code executes
* **configs/config.py** : This holds configuration values like the specifications of the input data, the location of the input file and the path of the output file. By convention the locations should be in their respective folders. Technically putting the values to any valud folder path would work.
* **configs** : This folder holds all configurations including the configuration of the input file in json format *specs.json*
* **input** : All input data file is placed here. 
* **output** : All output data file is recieved here. 
* **parser** : The folder to hold all parsers. For the this project there is only one parser in it.
* **tests** : The placeholder for all testing related artifacts and code. This has data generators in ***data*** folder, unit tests in the  ***unit_tests*** folder, and all integration tests in the ***integration_tests*** folder.
* **Dockerfile** : The docker file used to run the application in a docker container.
* **.dockerignore** : The standard docker ignore file to ignore copying certain artifats to the docker container.
* **requirements.txt** : The list of python requirements
* **.gitignore** : All files to be ignored by git.

## Running the application
To run the default parsing with the input and output. After the installation and activating the environment, run the following command.

**Windows**
```bash
   py main.py
```
**Linux/ Macos**
```bash
   python main.py
```

In case you need to run a custom input data and specs file, follow the followig. 

### Prerequisits
* Installation steps have been run. 
* The specs file is located in a valid folder. Conventionally the file should be in the ***configs*** folder. There is already a sample file called ***configs/spec_purchase_history_data.json*** inplace.
* The valid input file is located in a valid location.  Conventionally the file should be in the ***input*** folder. There is already a sample file called ***input/spec_purchase_history_data.txt*** inplace.
* Make sure ***configs/config.py*** has the correct entry for 
  * input file path
  * output file path
  * specs file path
* Activate the venv environment as described in the installation section.

### Run the code

**Windows**
```bash
   py main.py
```
**Linux/ Macos**
```bash
   python main.py
```
### Checking the output
You can find output file as per the cofiguration in the ***configs/config.py*** file.

## Running the Tests

### Prerequisits
* Activate the venv environment as described in the installation section.

### Running All Tests

**Windows**
```bash
   py -m pytest
```
**Linux/ Macos**
```bash
   pytest
```

### Runnint Unit Tests

**Windows**
```bash
   py -m pytest tests/unit_tests
```
**Linux/ Macos**
```bash
   pytest ./tests/unit_tests
```


### Running Integration Tests

**Windows**
```bash
   py -m pytest tests/integration_tests
```
**Linux/ Macos**
```bash
   pytest ./tests/integration_tests
```


## Running in Docker

### Prerequisits
* Docker should be installed on the system
  
### Build the container

```bash
docker build -t fw_app .
```
  
### Starting the image

```bash
docker run -it fw_app  /bin/bash
```
This will start the bash of the docker image
  
### Running the applications and tests
In the bash use the same commands as those under MacOs/Linux sections to run the application and tests.





