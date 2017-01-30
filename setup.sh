#!/bin/bash
#vim :set filencoding=utf-8:

virtualenv .venv
. .venv/bin/activate
pip install -r requirements.txt
deactivate