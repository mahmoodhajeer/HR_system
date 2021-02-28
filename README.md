# HR_system
Simple HR system, where job applicants can register as potential candidates and upload their resumes, and HR managers can log in and see the list of candidates and download their resumes.

to How to setup the database mariaDB server and run :
$ brew update  //to make sure you have the latest Version of HOMEBREW
$ brew install mariadb //to install mariaDB server
$ mysql.server start// to start the server
$ mysql -u root -p // to get into database as root user
then enter the password 'root'

$CREATE DATABASE HR_system; //to create database with name HR_system

get to the file code direction and run the folowing cmd to create database table:
$ python migrate.py db init
$ python migrate.py db migrate 
$ python migrate.py db upgrade 

then you can run the app by run:
$ python run.py