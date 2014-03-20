ReCap
===========
Start off by cloning the repository to your local workspace:<br>
git clone https://github.com/spinakr/DIM3_team-as.js.git <br>

Go into the newly created directory: <br>
cd DIM3_team-as.js <br>

Then create a new virtual environment, activate it and import the python requirements: <br>
virtualenv recap-env <br>
source recap/bin/activate <br>
pip install -r requirements.txt <br>

When this is done, sync the datbase and run the population script: <br>
python manage.py syncdb <br>
python populate_recap.py <br>

Finaly, run the server.: <br>
python manage.py runserver <br>

The app should now be accessible at localhost:8000/recap <br>

There are three test-users allready in the system, these are: <br>
clive, decanter and snotty - all with password "12345".
