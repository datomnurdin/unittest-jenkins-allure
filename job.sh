#!/bin/bash

echo '#### Create Virtual Environment ####'
VIRTUAL_ENV_NAME='virtual-environment'
virtualenv $VIRTUAL_ENV_NAME

echo '#### Activate Virtual Environment ####'
source $VIRTUAL_ENV_NAME/bin/activate

echo '#### Install requirements ####'
pip install -r requirements.txt

echo '#### Run tests ####'
python3 --alluredir=allure-results tests.py  

echo ### deactivate virtual environment ###
deactivate