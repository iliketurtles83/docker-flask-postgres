from flask.cli import FlaskGroup

from project import create_app
from project.models import db

app = create_app()

cli = FlaskGroup(app)

@cli.command("recreate_db")
def recreate_db():
    '''Recreate the database'''
    db.reflect()
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("create_db")
def create_db():
    '''Create the database'''
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("update_db")
def update_db():
    '''Update the database'''
    db.reflect()
    db.session.commit()

if __name__ == "__main__":
    cli()