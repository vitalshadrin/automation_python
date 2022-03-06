1. Check you python version. Open terminal and set next commons

- Windows : **py --version**
- Linux : **python --version**

if the command does not return a result, please install python:

- Windows :
  Download and install last python version from [python](https://www.python.org/downloads/windows/)

- Linux :
  Open terminal and run the following command: **sudo apt install python3**

2. Installing pip
   To manage Python software packages, need to install the _pip_ tool

- Windows :
  The Python installers for Windows include pip. You should be able to access pip using:
  **py -m pip --version**
  _pip 9.0.1 from c:\python36\lib\site-packages (Python 3.6.1)_

  You can make sure that pip is up-to-date by running:
  **py -m pip install --upgrade pip**

- Linux :
  Open terminal and run the following command: **python3 -m pip install --user --upgrade pip**
  Afterwards, you should have the newest pip installed in your user site:
  **python3 -m pip --version**
  _pip 9.0.1 from $HOME/.local/lib/python3.6/site-packages (python 3.6)_

3. Installing virtualenv
   _virtualenv_ is used to manage Python packages for different projects. Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects. You can install virtualenv using pip.

- Windows :
  Open terminal and run the following command: **py -m pip install --user virtualenv**

- Linux :
  Open terminal and run the following command: **python3 -m pip install --user virtualenv**

4. Creating a virtual environment
   To create a virtual environment, go to your project’s directory and run venv

- Windows :
  Open terminal and run the following command: **py -m venv env**

- Linux :
  Open terminal and run the following command: **python3 -m venv env**

5. Activating a virtual environment
   Before you can start installing or using packages in your virtual environment you’ll need to activate it. Activating a virtual environment will put the virtual environment-specific python and pip executables into your shell’s PATH.

- Windows :
  Open terminal and run the following command: **.\env\Scripts\activate**

- Linux :
  Open terminal and run the following command: **source env/bin/activate**

6. Install all required dependencies

   | Windows                             | Linux                                |
   | ----------------------------------- | ------------------------------------ |
   | **pip install -r requirements.txt** | **pip3 install -r requirements.txt** |
