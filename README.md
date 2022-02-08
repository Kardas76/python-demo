## General info
This project is python-based electric analizator client with modbus communication.
	
## Technologies
Project is created with:
* Python 3.8.10 32 bit
* PySide2
* QT Designer 5.12

## Requirements
Install Python by visiting [this site](https://www.python.org/downloads/).


It is recommended to create local environment each project. To do this, type:


Using virtualenv:
```
pip install virtualenv
virtualenv project_environment_name
.project_environment_name/Scripts/Activate.ps1
```

To install necessary pip packages, run:
```
python -m pip install -r requirements.txt
```

Uninstalling all packages:
```
python -m pip uninstall -r requirements.txt -y
```


Exporting pip packages to file from local environment:
```
python -m pip freeze --local > requirements.txt
```

Exporting pip packages to file:
```
python -m pip freeze > requirements.txt
```


Alternatively you can use pipenv to create virtual environment:
```
pip install pipenv
pipenv install
pipenv shell
```
	
## Runnig
To run this project, type in console:
```
$ python main.py
```

To copy auto-generated files by QT Designer run script:
```
.\replace_generated.bat
```

## Files specification

<mark>.qrc</mark> - resources file edited in QT Designer

<mark>.ui</mark> - QT Designer form

<mark>ui_*.py</mark> - QT Designer generated tools

## Standalone compiling

Make sure you added PyInstaller to system path, and then run:

```
cd .\standalone_build\

.\standalone_build.bat
```