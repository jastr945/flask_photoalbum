from flask_script import Manager
from project import create_app, db
import unittest
from project.api.models import Album, Image


app = create_app()
manager = Manager(app)

@manager.command
def recreate_db():
    """Recreates a database."""
    db.drop_all()
    db.create_all()
    db.session.commit()


@manager.command
def test():
    """Runs the tests without code coverage."""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def seed_db():
    """Seeds the database."""
    album1 = Album(title='polina', description="Polina's album with many awesome pictures.")
    img1 = Image(name='pigs3.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/880e033191ca56e1612049fcf76565b7a8377911/subscriber/coffee5.jpg')
    img2 = Image(name='pigs4.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/880e033191ca56e1612049fcf76565b7a8377911/subscriber/coffee2.jpg')

    album2 = Album(title='pofi', description="Pofi's cute pictures.")
    img3 = Image(name='pigs7.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/880e033191ca56e1612049fcf76565b7a8377911/subscriber/coffee.jpg')
    img4 = Image(name='pigs8.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/880e033191ca56e1612049fcf76565b7a8377911/subscriber/coffee4.jpg')

    album1.images = [img1, img2]
    album2.images = [img3, img4]

    db.session.add(album1)
    db.session.add(album2)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
