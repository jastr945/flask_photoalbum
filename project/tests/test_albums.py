import json
from project.tests.base import BaseTestCase
from project import db
from project.api.models import Album, Image
import datetime
from oauth2client.file import Storage


def add_album(title, description, user_email, created_at=datetime.datetime.now()):
    album = Album(title=title, description=description, user_email=user_email, created_at=created_at)
    img1 = Image(name='img1.jpg', url='http://1')
    img2 = Image(name='img2.jpg', url='http://2')
    album.images = [img1, img2]
    db.session.add(album)
    db.session.commit()
    return album

def authorize():
    # storage for Google access token
    storage = Storage('credentials_file')
    storage.put({"email": "example@example.com"})
    return storage


class TestAlbumService(BaseTestCase):
    """Tests for the Albums Service."""

    def test_invalid_add_code(self):
        """Ensure error is thrown if invalid access code is sent."""
        with self.client:
            response = self.client.post(
                '/google',
                data=json.dumps({"headers": {"Authorization": {}}}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_authorized_empty(self):
        """Sending empty data if the user is not authorized."""
        with self.client:
            response = self.client.get('/googleauthorized')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('', data['data']['email'])
            self.assertIn('', data['data']['pic'])
            self.assertIn('success', data['status'])

    def test_add_album_unauthorized(self):
        """Ensure error is thrown if the user is not authorized."""
        with self.client:
            response = self.client.post(
                '/albums',
                data=json.dumps(dict(
                    title='test',
                    description='test album'
                )),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 403)
            self.assertIn('Unauthorized access. Please log in.', data['message'])
            self.assertIn('fail', data['status'])

    # def test_add_album_invalid_json(self):
    #     """Ensure error is thrown if the JSON object is empty.""" # authorization required
    #     with self.client:
    #         response = self.client.post(
    #             '/albums',
    #             data=json.dumps(dict()),
    #             content_type='application/json',
    #         )
    #         data = json.loads(response.data.decode())
    #         self.assertEqual(response.status_code, 400)
    #         self.assertIn('Invalid payload.', data['message'])
    #         self.assertIn('fail', data['status'])
    # #
    # def test_add_album_invalid_json_keys(self):
    #     """Ensure error is thrown if the JSON object does not have a title key."""
    #     with self.client:
    #         response = self.client.post(
    #             '/albums',
    #             data=json.dumps(dict(title='jastr945')),
    #             content_type='application/json',
    #         )
    #         data = json.loads(response.data.decode())
    #         self.assertEqual(response.status_code, 400)
    #         self.assertIn('Invalid payload.', data['message'])
    #         self.assertIn('fail', data['status'])
    #
    # def test_add_album_duplicate_album(self):
    #     """Ensure error is thrown if the title already exists."""
    #     with self.client:
    #         self.client.post(
    #             '/albums',
    #             data=json.dumps(dict(
    #                 title='jastr945',
    #                 description='my album'
    #             )),
    #             content_type='application/json',
    #         )
    #         response = self.client.post(
    #             '/albums',
    #             data=json.dumps(dict(
    #                 title='jastr945',
    #                 description='my album'
    #             )),
    #             content_type='application/json',
    #         )
    #         data = json.loads(response.data.decode())
    #         self.assertEqual(response.status_code, 400)
    #         self.assertIn(
    #             'Sorry. That album already exists.', data['message'])
    #         self.assertIn('fail', data['status'])
    #
    def test_delete_album_unauthorized(self):
        """Ensure error is thrown if unauthorized user deletes album."""
        with self.client:
            response = self.client.delete('/albums/test')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 403)
            self.assertIn('Unauthorized access. Please log in.', data['message'])
            self.assertIn('fail', data['status'])

    # def test_delete_nonexistent_album(self):
    #     """Ensure error is thrown if the title does not exist."""
    #     add_album('pofi', 'cats album', 'example@example.com')
    #     with self.client:
    #         response = self.client.delete('/albums/pofi1')
    #         data = json.loads(response.data.decode())
    #         self.assertEqual(response.status_code, 404)
    #         self.assertIn('Album does not exist.', data['message'])
    #         self.assertIn('fail', data['status'])

    def test_get_all_albums(self):
        """Ensure get all albums behaves correctly."""
        created = datetime.datetime.now() + datetime.timedelta(-30)
        add_album('jastr945', 'my album', 'example@example.com', created)
        add_album('pofi', 'cats album', 'example@example.com')
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
            self.assertIn('example@example.com', data['data']['albums'][0]['user_email'])
            self.assertIn('example@example.com', data['data']['albums'][1]['user_email'])
            self.assertIn('success', data['status'])
