# DOCUMANAGER
A rest api server made in Django 4 by Saul Maldonado
## How to build the environment
1. You must need python +3.8 installed in your machine
2. Create and activate a virtual environment
```bash
python3 -m venv /path/to/new/virtual/environment
venv\\Scripts\\activate.bat (windows)
```
3. Install required packages
```bash
pip install -r requirements.txt
```

## How to run the application
1. Run the application
```bash
python manage.py runserver
```

## Run it on Docker
1. Run and build the application (you need Docker installed in your machine)
```bash
docker-compose up -d --build
```

# About this project
## To access admin panel
Open http://127.0.0.1:8000/admin/ on a browser
- Django superSaul.123.!user: admin
- Django password: @dm!n.123

## Users
3 default users comes
```bash
* Gemma
* Brendan
* Saul
```
All users have the same password: Propylon2022

## How documents are saved
Uploaded files are saved in media/documents/ folder where:
```
* Every user will have a unique folder based on the user id.
* The original version will be saved in that folder.
* For future revisions an unique subfolder will be created for every document (based on the document id).
* Every revision will represent a version of the original document that will be saved in a unique subfolder as well
* Examples:
  - media/documents/3/document.pdf: 
    User with id "3" has saved a document.pdf for the first time.
    
  - media/document/3/10/v1/document.pdf:
    User with id "3" has saved a revision as the first version "v1" of document.pdf with document id "10"

Note: Files will not be overriden when having the same name because Django will add a random trailing text 
      to the second file name.
```

## Testings the code
From project's root directory start the server
```bash
python manage.py runserver
```
Run tests
```bash
python manage.py test --pattern="*_test.py" documanager\all_tests
```

## Out of this scope 
* Users can't be updated, or deleted
* Login has no security

## Known Bugs
Documents and revisions can't be updated nor deleted
* Django is not allowing to deal with PUT and DELETE http requests.
