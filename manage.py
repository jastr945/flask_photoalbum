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
    album1 = Album(title='Columbia River Gorge', description='The Columbia River Gorge is a canyon of the Columbia River in the Pacific Northwest of the United States.', user_email='example@example.com')
    img1 = Image(name='1.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Columbia_River_Gorge/DSC03751.JPG')
    img2 = Image(name='2.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Columbia_River_Gorge/DSC03754.JPG')
    img3 = Image(name='3.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Columbia_River_Gorge/DSC03755.JPG')
    img4 = Image(name='4.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Columbia_River_Gorge/DSC03756.JPG')

    album2 = Album(title='Crystal Springs Rhododendron Garden', description='Beautiful rhododendron garden in gorgeous Southeast Portland!', user_email="example@example.com")
    img5 = Image(name='5.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Crystal_Springs_Rhododendron_Garden/DSC03714.JPG')
    img6 = Image(name='6.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Crystal_Springs_Rhododendron_Garden/DSC03715.JPG')
    img7 = Image(name='7.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Crystal_Springs_Rhododendron_Garden/DSC03719.JPG')
    img8 = Image(name='8.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Crystal_Springs_Rhododendron_Garden/DSC03723.JPG')
    img9 = Image(name='9.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Crystal_Springs_Rhododendron_Garden/DSC03726.JPG')
    img10 = Image(name='10.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Crystal_Springs_Rhododendron_Garden/DSC03727.JPG')
    img11 = Image(name='11.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Crystal_Springs_Rhododendron_Garden/DSC03735.JPG')
    img12 = Image(name='12.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Crystal_Springs_Rhododendron_Garden/DSC03741.JPG')
    img13 = Image(name='13.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Crystal_Springs_Rhododendron_Garden/DSC03744.JPG')
    img14 = Image(name='14.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Crystal_Springs_Rhododendron_Garden/DSC03745.JPG')
    img15 = Image(name='15.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Crystal_Springs_Rhododendron_Garden/DSC03746.JPG')

    album3 = Album(title='Magnolia Trail in the Washington Park', description='Hoyt Arboretum, Portland, Oregon. Spring 2018.', user_email='example@example.com')
    img16 = Image(name='16.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Magnolia_Trail_in_the_Washington_Park/DSC03639.JPG')
    img17 = Image(name='17.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Magnolia_Trail_in_the_Washington_Park/DSC03642.JPG')
    img18 = Image(name='18.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Magnolia_Trail_in_the_Washington_Park/DSC03643.JPG')
    img19 = Image(name='19.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Magnolia_Trail_in_the_Washington_Park/DSC03644.JPG')
    img20 = Image(name='20.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Magnolia_Trail_in_the_Washington_Park/DSC03655.JPG')
    img21 = Image(name='21.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Magnolia_Trail_in_the_Washington_Park/DSC03654.JPG')
    img22 = Image(name='22.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Magnolia_Trail_in_the_Washington_Park/DSC03660.JPG')

    album1.images = [img1, img2, img3, img4]
    album2.images = [img5, img6, img7, img8, img9, img10, img11, img12, img13, img14, img15]
    album3.images = [img16, img17, img18, img19, img20, img21, img22, img13]

    db.session.add(album1)
    db.session.add(album2)
    db.session.add(album3)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
