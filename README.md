# VR-Sensors MQTT Brokker

VR 3D data analytic project

## Installation

The first step is to install FastAPI in your computer but before this you need a virtual environment for run the project. so Create a directory in you computer where you want to keep your project. Open Command Promt (Terminal) in windows machine(computer). First, create a directory for your project. using "mkdir vrsensor_api" then use "cd vrsensor_api" then create virtual environment inside the directory by using the below command

```bash
python -m venv pvenv    
```

Here "pvenv" is the virtual environment folder. after excute above command some files will created in this folder. now You need to activate the virtual environment for run the fastapi project that will create later on.

 ```bash
pvenv\Scripts\activate.bat
```

After activate virtual environment. Check that the virtual environment is active (the previous command worked).
If it shows the python binary at pvenv\Scripts\python, inside of your project folder (in this case vrsensor_api), then it worked fine. if your pip is not updated you can update your pip library by using below command. for successfully complete these all step you should have installed python library otherwise will not work above command.

```bash
python -m pip install --upgrade pip
```

## Now You need to install fastapi framework. 

```bash
pip install fastapi[standard]
```

We create new one or update the existing requirements.txt file for update all dependency package that need in our project. Use this below command for that
 
```bash
pip freeze > requirements.txt
```

Now you can create main.py file in your project or if you install this repository then just download these project and run the downloaded project using this command. Here main.py is the start path file.

```bash
fastapi dev main.py
```

or you can run the project using below command 


```bash
fastapi dev main.py --host 127.0.0.1 --port 8080
```

## Usage
 

## Contributing

 

## License

 