# nba-team-api

## Local setup
Create a virtualenv at the project root

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

Install postgres locally, if needed

    brew install postgres
    pg_ctl -D /usr/local/var/postgres start

Create a new role and database for this app

    psql -d postgres
    create role nbateam with login password='localpassword'`
    create database nbateam with owner nbateam
    \q (to exit)

Login to verify connecting to the new database (there won't be any tables yet)

    psql -d nbateam -U nbateam

Exit out of psql and set some required environment variables:

    export FLASK_APP=/path/to/manage.py
    export SECRET_KEY=this-is-the-local-key
    export FLASK_DEBUG=1
    export DATABASE_URL=postgresql://localhost:5432/nbateam (fill in credentials, etc.)

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
