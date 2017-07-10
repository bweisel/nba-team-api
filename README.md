# nba-team-api

## Local setup
Create a virtualenv

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

Create a postgres database

    TODO: write instructions

Set some required environment variables:

    export FLASK_APP=/path/to/manage.py
    export SECRET_KEY=this-is-the-local-key
    export FLASK_DEBUG=1
    export DATABASE_URL=sqlite:////path/to/code/root/nba-team-api/nbateam.db

Setup the database:

    flask db init (only run once)
    flask db migrate
    flask db upgrade
    TODO: create db dump and put instructions on how to load

Run the API server locally:

    flask run

And test it out:

    curl localhost:5000/api/players/1824

If you want to update the stats:

    TODO: write instructions
