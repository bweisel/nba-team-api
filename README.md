# nba-team-api

## Local setup
Create a virtualenv

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

Set some required environment variables:

    export FLASK_APP=/path/to/manage.py
    export SECRET_KEY=this-is-the-local-key
    export FLASK_DEBUG=1
    export DATABASE_URL=sqlite:////path/to/code/root/nba-team-api/nbateam.db

Then setup the database (sqlite for local dev):

    flask db init
    flask db migrate
    flask db upgrade
    flask run

Then run the following commands to bootstrap your environment:

    git clone https://github.com/bweisel/what-to-do
    cd what-to-do
    pip install -r requirements.txt
    flask run
