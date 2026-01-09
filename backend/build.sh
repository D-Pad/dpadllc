#!/bin/bash 


# This script is for development only


# Initial setup
[[ ! -d /usr/local/venvs ]] && mkdir /usr/local/venvs
[[ ! -d /usr/local/venvs/webpage ]] && \
  python -m venv /usr/local/venvs/webpage && \
  source /usr/local/venvs/webpage/bin/activate && \
  pip install -r ./app/requirements.txt && \
  deactivate

# App start
source /usr/local/venvs/webpage/bin/activate
cd app
python main.py
deactivate


