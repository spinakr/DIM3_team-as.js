ReCap
===========
Start off by cloning the repository to your local workspace:
git clone https://github.com/spinakr/DIM3_team-as.js.git

Then create a new virtual environment, activate it and import the python requirements:
mkvirtualenv ReCap
workon ReCap
pip -r requirements.txt

When this is done, sync the datbase and run the population script:
python manage.py syncdb
python populate_recap.py

Finaly, run the server.:
python manage.py runserver

The app should now be accessible at localhost:8000/recap
