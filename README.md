You can see the project live on www.calculatorpro.co

To install the project locally, please begin by installing Docker Engine and Docker Compose.
https://docs.docker.com/engine/install/ubuntu/

Then run the following commands:

cd calculator-logs

docker build .

docker-compose build

docker-compose up

_______________________________________________________

Alternatively, you can install virtual environment:

cd calculator-logs/calculator

sudo apt-get install virtualenv

virtualenv venv

source venv/bin/activate

pip install -r ../requirements.txt

python3 manage.py collectstatic

python3 manage.py migrate

python3 manage.py runserver
