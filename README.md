# Dreamkas QA Test
## Description
This repo is an answer to a quest of becoming QA in Dreamkas.
## Setup
Install python, pip and virtualenv:
```bash
sudo apt-get install python3-pip
sudo pip install virtualenv
```
Launch the setup script:
```bash
bash setup.sh
```
## Run tests
Activate the virtual environment:
```bash
. .venv/bin/activate
```
Now you may run tests as much as you want:
```bash
pytest
```
When you are done with testing, deactivate the venv:
```bash
deactivate
```