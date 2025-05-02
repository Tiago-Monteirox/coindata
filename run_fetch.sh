#!/bin/bash

cd /home/tiagomonteiro/projects/coindata_project
source env/bin/activate

export $(cat .env | xargs)


/home/tiagomonteiro/projects/coindata_project/env/bin/python manage.py fetchbtc
