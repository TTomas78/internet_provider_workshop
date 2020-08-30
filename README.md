# Taller-Python
Taller de python

# Pasos para la instalacion:

1 - install virtualenv

  sudo apt install virtualenv
  
2 - create the virtual environment

  virtualenv venv
  
  or specify the python version you want
  
  virtualenv venv -p /usr/bin/python3.7
  
3 - open the virtual environment

  source venv/bin/activate

4 - install mysql client for python

  sudo apt-get install libmysqlclient-dev
  
5 - install the requirements

  pip install -r requirements.txt
  
  
6 - install docker following the instuctions

  https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository

7 - install docker compose

  sudo apt install docker-compose
  
8 - restart your computer

9 - raise the docker containers

  docker-compose up -d
  
10 run the migrations

  source ./run.local
  
  stop the server (that step it's because you need to set the enviroments variables into your terminal session)
  
  flask db upgrade
  
10 - run the application

  ./run.local
  
11 - open the documentation page in your browser

  localhost:5000/docs

