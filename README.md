# VenYou

Our web app aims to let people discover, rate and give opinions on clubs and venues in their area.

Everyone can find venues in their area and see how they score in the categories vibe, hygiene and safety.


# Virtual Environment Versions

Python 3.9
Django 2.2.26

# How to setup

1. Create a virutal environment with Python 3.9. This can be done by `conda create -n venyou python=3.9`.

2. Then install the dependencies. A list of the requirements can be found in `requirement.txt` and and can be installed with `pip install -r requirements.txt`.

3. Create and populate the datebase by running `database_setup.bat` or `database_setup.sh` or by running the commands in these files individully.

4. Run the server with `python venyou/manage.py runserver`.

# How to run tests

Run the command `python venyou/manage.py test venyou_app`

# Superuser details

Username: admin
Password: password

Username: VenYou
Password: Venue_Team12C