# Rater
>Developed by [Michelle-Njeri](https://github.com/vantablanta)  
  
## Description  
>An application that allows a user to post a project he/she has created and get it reviewed by his/her peers.

##  Live Link  
>[View Site](https://gram-mn.herokuapp.com)  to visit the site
  

## User Story  
  
* Sign in to the application to start using.
* Upload a project to the application.
* See your profile section.
* See reviews your project has recieved 
* Review other people's projects
    
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
```bash 
 https://github.com/vantablanta/rater.git
```
##### Navigate into the folder
 ```bash 
cd project-gram
```
##### Install and activate Virtual  
 ```bash 
pipenv shell 
```  
##### Install Dependencies  
 ```bash 
 pipenv sync
```  
##### Setup Database  
  SetUp your database User,Password, Host then make migrations 
 ```bash 
python manage.py makemigrations app
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 4.0](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [vantablanta@gmail.com]  
  
## License 

[![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/vantablanta/rater/blob/master/LICENSE)  
>Copyright (c) 2022 **Michelle Njeri**