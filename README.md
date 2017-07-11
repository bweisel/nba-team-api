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

Exit out of psql and set some required environment variables

    export FLASK_APP=/path/to/manage.py
    export SECRET_KEY=this-is-the-local-key
    export FLASK_DEBUG=1
    export DATABASE_URL=postgresql://localhost:5432/nbateam (fill in credentials, etc.)

Setup the database:

    flask db init (only run once)
    flask db migrate
    flask db upgrade

Import the database dump file

    pg_restore --verbose --clean --no-acl --no-owner -h localhost -U nbateam -d nbateam nbateam.dump

Run the API server locally

    flask run

And test it out

    curl localhost:5000/api/players/1824


## Maintenance
If you want to update the stats

    TODO: write instructions

To capture a backup from heroku and apply to local

    heroku pg:backups:capture --app nba-team-api
    heroku pg:backups:download --app nba-team-api

To apply a local backup to heroku

    pg_dump -Fc --no-acl --no-owner -h localhost -U nbateam nbateam > nbateam.dump
    Upload the dump to S3
    heroku pg:backups restore --app nba-team-api 'https://s3-us-west-2.amazonaws.com/nba-team-api/nbateam.dump' DATABASE_URL