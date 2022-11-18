# Project Objective
### The aim is to apply ORM techniques in developing an executable program to manage inventory and sales data using python library *pymyql* and GUI framework *tkinter*.
# Stack
* Python
* Pymysql
* Tkinter
* Unittest
# Workflow
![workflow](https://user-images.githubusercontent.com/83990919/202628715-71905520-9ae3-4d20-bcfd-6e7666849680.png)
### Project directory
1. Create a project directory using the command line
2. Create a virtual environment
3. Activate virtual environment
### Install dependencies
pip install the following
1. tkinter
2. pymysql
3. cryptography
4. unittest
5. pyinstaller
### .py Database file
1. import dependencies (pymsql and configparser)
   * #### *pymysql* - a python library for connecting to MYSQL relational database.
   * #### *configparser* - python library for reading *.ini* files. *.ini* files store program-dependent data in a key and value format.
2. Using Object Oriented programming, create a class for database encapsulating methods for *connecting, inserting, fetching, updating, removing and deleting operations*.
### .py Database Test file
1. Create a .py test file, then import unittest and .py database file into the script.
2. Create a test class containing methods for testing each database function
### .py Tkinter file
1. import dependencies (tkinter and .py database file)
2. using tkinter methods, develop a program to effectively connect to MySQL database through the class methods of .py database file.
### Note
To create an executable file for your project, run the following line on the terminal
* pyinstaller tkinterfilename.py --onefile --windowed
# Summary
Using the process as outlined, a well responsive software for inventory and sales management can be developed as well as any GUI database management problem can be solved approaching with same principle.
