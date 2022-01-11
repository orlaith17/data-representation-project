# Data-Representation-Big-Project
Project Submission for the Data Representation module at GMIT 2021
Orla Higgins G00364860

My project is based on a hypothetical sports club which can retrieve data from a MySQL database called sportsclub. Within this database there are four tables of data, two are linked by foreign key references. 

## Python Anywhere

This project is hosted on Python Anywhere at the below links:

http://orlaith17.pythonanywhere.com/

#### Web Pages:

Index: https://orlaith17.pythonanywhere.com/index.html

Members: https://orlaith17.pythonanywhere.com/members.html

Stock: https://orlaith17.pythonanywhere.com/stock.html

Login: https://orlaith17.pythonanywhere.com/admin (an unrealised attempt at logging in)

## To view on local machine

After you have my server up and running (details later in this file) in your local machine go to:

Login: http://127.0.0.1:5000/index.html

Members: http://127.0.0.1:5000/members.html

Stock: http://127.0.0.1:5000/stock.html

## Contents of this repository

This repository contains:

* **initdb.sql** - The commands used to create the database and tables in MySQL.
* **sportsclubDAO.py** - Python DAO file to connect to the MySQL database and retrieve data from the database.
* **testSportsclubDAO.py** - Python file to test sportsclubDAO.py manually with direct input values.
* **server.py** - Python App server which should be run in a virtual environment.
* Static pages which serve up the data to the user in a web browser and allow the user to perform CRUD operations on the data. 
    * **index.html** - homepage
    * **members.html** - members page which contains the data retrieved from the members table in the sportsclub database. The user can perform CRUD operations on the data through the members.html page. 
    * **stock.html** - stock page which contains the data retrieved from the stock table in the sportsclub database. The user can perform CRUD operations on the data through the members.html page. 
    * **login.html** - JSON objects of the admins in the sportsclub database
* **dbconfigtemplate.py** - a file that should hold the log in credentials to be read by the Python DAO file to connect to the MySql database.
* **requirements.txt** - contains the list of required packages that should be installed in a virtual environment in order for this server to run.
* **.gitignore** file which are not part of a git push.
* **README.md** file instructing how to operate server. 

## Virtual Environment 

This repository consists of a server which should be run in a virtual environment.

#### Running a VM for the first time on your machine

The command to  install a virtual environment on your machine for the first time are as follows:

1. python -m venv venv

2. .\venv\Scripts\activate.bat

To install the requires packages:

3. pip install -r requirements.txt

To run my server:

4. python server.py

To exit the virtual environment:

5. deactivate

#### If you already have a VM installed on your machine

1. Pull my project from Github and navigate to the folder location.

2. .\venv\Scripts\activate.bat

3. python server.py

To exit the virtual environment:

4. deactivate

## How to clone this repository

1. Go to GitHub.
2. Go to my repository: https://github.com/orlaith17/data-representation-project
3. Click the Code button which is colored green.
4. Click on HTTPS and copy the link that is shown. 
5. Open the command line on your machine, navigate to the directory where you would like to clone the repository down to.
6. Enter the command: git clone followed by the URL of the repository.
7. The repository will be cloned down to your current working directory. 
8. You will need to navigate to this folder location on the command line in order to run the program.

## MySQL Database 

I have created a MySQL database called sportsclub which will contain details on members and stock of the club. 

I have created four tables of data: 
1. Location
2. Members
3. Stock
4. Admin

Location and Members are linked by a foreign key. 

The commands that were used to create the database and table and insert data into the table are saved in the folder SQL in this repository in a file called initdb.sql

#### location table - served to BullViewer.html
* The id of each location which is auto incremented and serves as the primary key. 
* The location contains name of the location. 

#### members table - served to BullDetails.html
* The id of each member which is auto incremented and serves as the primary key. 
* Name
* Age
* Gender
* Location which acts as a foreign key to the location

#### stock table - served to BullDetails.html
* The id of each stock which is auto incremented and serves as the primary key. 
* Name
* Description
* Price

#### admin table - served to BullDetails.html
* The id of each admin which is auto incremented and serves as the primary key. 
* Name
* Password 



