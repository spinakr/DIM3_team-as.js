ReCap
===========
Start off by cloning the repository to your local workspace:<br>
git clone https://github.com/spinakr/DIM3_team-as.js.git <br>

Then create a new virtual environment, activate it and import the python requirements: <br>
mkvirtualenv ReCap <br>
workon ReCap <br>
pip install -r requirements.txt <br>

When this is done, sync the datbase and run the population script: <br>
python manage.py syncdb <br>
python populate_recap.py <br>

Finaly, run the server.: <br>
python manage.py runserver <br>

The app should now be accessible at localhost:8000/recap <br>
