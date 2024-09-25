#!/bin/sh

# Cria o ambiente virtual do programa
python -m venv env
source env/bin/activate
sudo pacman -S tesseract
pip install -r requirements.txt
source env/bin/deactivate
