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
    album1 = Album(title='Example Gallery: Columbia River Gorge', description='The Columbia River Gorge is a canyon of the Columbia River in the Pacific Northwest of the United States.', user_email='example@example.com')
    img1 = Image(name='1.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Columbia_River_Gorge/DSC03751.JPG')
    img2 = Image(name='2.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Columbia_River_Gorge/DSC03754.JPG')
    img3 = Image(name='3.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Columbia_River_Gorge/DSC03755.JPG')
    img4 = Image(name='4.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Columbia_River_Gorge/DSC03756.JPG')

    album2 = Album(title='Example Gallery: Crystal Springs Rhododendron Garden', description='Beautiful rhododendron garden in gorgeous Southeast Portland!', user_email="example@example.com")
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

    album3 = Album(title='Example Gallery: Magnolia Trail in the Washington Park', description='Hoyt Arboretum, Portland, Oregon. Spring 2018.', user_email='example@example.com')
    img16 = Image(name='16.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Magnolia_Trail_in_the_Washington_Park/DSC03639.JPG')
    img17 = Image(name='17.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Magnolia_Trail_in_the_Washington_Park/DSC03642.JPG')
    img18 = Image(name='18.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Magnolia_Trail_in_the_Washington_Park/DSC03643.JPG')
    img19 = Image(name='19.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Magnolia_Trail_in_the_Washington_Park/DSC03644.JPG')
    img20 = Image(name='20.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Magnolia_Trail_in_the_Washington_Park/DSC03655.JPG')
    img21 = Image(name='21.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Magnolia_Trail_in_the_Washington_Park/DSC03654.JPG')
    img22 = Image(name='22.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Magnolia_Trail_in_the_Washington_Park/DSC03660.JPG')

    album4 = Album(title='Example Gallery: Portland Japanese Garden', description='This place is considered to be the most authentic Japanese Garden outside of Japan.', user_email='example@example.com')
    img23 = Image(name='23.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Japanese_Garden/DSC03668.JPG')
    img24 = Image(name='24.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Japanese_Garden/DSC03678.JPG')
    img25 = Image(name='25.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Japanese_Garden/DSC03688.JPG')

    album5 = Album(title='Example Gallery: The Mt. Hood National Forest', description='The Mt. Hood National Forest is 20 miles away from Portland.', user_email='example@example.com')
    img26 = Image(name='26.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Mount_Hood/DSC03233.JPG')
    img27 = Image(name='27.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Mount_Hood/DSC03234.JPG')
    img28 = Image(name='28.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Mount_Hood/DSC03236.JPG')
    img29 = Image(name='29.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Mount_Hood/DSC03238.JPG')
    img30 = Image(name='30.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Mount_Hood/DSC03239.JPG')
    img31 = Image(name='31.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Mount_Hood/bird.jpg')
    img32 = Image(name='32.jpg', url='https://raw.githubusercontent.com/jastr945/xperiments/master/flask-photoalbum/sample_albums/Mount_Hood/mt_hood.jpg')

    album1.images = [img1, img2, img3, img4]
    album2.images = [img5, img6, img7, img8, img9, img10, img11, img12, img13, img14, img15]
    album3.images = [img16, img17, img18, img19, img20, img21, img22]
    album4.images = [img23, img24, img25]
    album5.images = [img26, img27, img28, img29, img30, img31, img32]

    db.session.add(album1)
    db.session.add(album2)
    db.session.add(album3)
    db.session.add(album4)
    db.session.add(album5)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
