# SEVC Scrapper

This script connects to the official Southern European Veterinary Conference (2019) and scrapes the web finding all the lectures given in the conference.

These lectures will be saved as PDF organized by Categories. (Spanish lenguage will be used)

All the contents will be available under `contents` directory.

## Requirements

* Python 3+
* Pip
* Pipenv

Then run `pipenv install` for install all the required dependencies defined in the **Pipfile** file

## Launching the script

```curl
pipenv run python3 scrapper.py
``` 