import json

from project.tests.base import BaseTestCase
from project import db
from project.api.models import Album
import datetime


def add_album(title, description, created_at=datetime.datetime.now()):
    album = Album(title=title, description=description, created_at=created_at)
    db.session.add(album)
    db.session.commit()
    return album


class TestAlbumService(BaseTestCase):
    """Tests for the Albums Service."""

    def test_albums(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('kittykats!', data['message'])
        self.assertIn('success', data['status'])

    def test_add_album(self):
        """Ensure a new album can be added to the database."""
        with self.client:
            response = self.client.post(
                '/albums',
                data=json.dumps(dict(
                    title='jastr945',
                    description='my album'
                )),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('jastr945 was added!', data['message'])
            self.assertIn('success', data['status'])

    def test_add_album_invalid_json(self):
        """Ensure error is thrown if the JSON object is empty."""
        with self.client:
            response = self.client.post(
                '/albums',
                data=json.dumps(dict()),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_album_invalid_json_keys(self):
        """Ensure error is thrown if the JSON object does not have a title key."""
        with self.client:
            response = self.client.post(
                '/albums',
                data=json.dumps(dict(title='jastr945')),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_album_duplicate_album(self):
        """Ensure error is thrown if the title already exists."""
        with self.client:
            self.client.post(
                '/albums',
                data=json.dumps(dict(
                    title='jastr945',
                    description='my album'
                )),
                content_type='application/json',
            )
            response = self.client.post(
                '/albums',
                data=json.dumps(dict(
                    title='jastr945',
                    description='my album'
                )),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn(
                'Sorry. That album already exists.', data['message'])
            self.assertIn('fail', data['status'])

    def test_single_album(self):
        """Ensure get single album behaves correctly."""
        album = add_album('jastr945', 'my album')
        with self.client:
            response = self.client.get(f'/albums/{album.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertTrue('created_at' in data['data'])
            self.assertIn('jastr945', data['data']['title'])
            self.assertIn('my album', data['data']['description'])
            self.assertIn('success', data['status'])

    def test_single_album_no_id(self):
        """Ensure error is thrown if an id is not provided."""
        with self.client:
            response = self.client.get('/albums/blah')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('Album does not exist', data['message'])
            self.assertIn('fail', data['status'])

    def test_single_album_incorrect_id(self):
        """Ensure error is thrown if the id does not exist."""
        with self.client:
            response = self.client.get('/albums/999')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('Album does not exist', data['message'])
            self.assertIn('fail', data['status'])

    def test_all_albums(self):
        """Ensure get all albums behaves correctly."""
        created = datetime.datetime.now() + datetime.timedelta(-30)
        add_album('jastr945', 'my album', created)
        add_album('pofi', 'cats album')
        with self.client:
            response = self.client.get('/albums')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['albums']), 2)
            self.assertTrue('created_at' in data['data']['albums'][0])
            self.assertTrue('created_at' in data['data']['albums'][1])
            self.assertIn('jastr945', data['data']['albums'][1]['title'])
            self.assertIn(
                'my album', data['data']['albums'][1]['description'])
            self.assertIn('pofi', data['data']['albums'][0]['title'])
            self.assertIn(
                'cats album', data['data']['albums'][0]['description'])
            self.assertIn('success', data['status'])
