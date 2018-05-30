# Photo Album

## Flask-React-Docker Microservices App

### Summary

This is a responsive web app where users can create personal image galleries.

The app is powered by Flask REST API, React.js and PostgreSQL, which run in separate containers as microservices, brought up by Docker Compose. Image sliders and the rest of the user interface were created from scratch in React. Login with Google (OAuth 2.0) is provided for creating private galleries.

### Demo

[Work in progress...]

### Specific Functionality

The environment consists of 3 services brought up by Docker Compose.

#### Python-Flask Backend

- Flask RESTful API allows users to add and delete image galleries;
- Multiple images can be saved into the database at once;
- OAuth 2.0 Client exchanges the authorization access code received from the client for the id token. The id token then exchanged for the user's credentials. User's email and profile picture are sent back to the client in a secure way.

#### React.js Frontend

- Image sliders created from scratch in a loop (map function);
- One image at a time can be expanded for a full-screen view;
- Multiple images can be selected and sent to the server at once;
- Each album has a time stamp, showing how long ago it was created;
- `Login with Google` button sends the authorization access code to the server.

#### Database

PostgreSQL database runs in a separate container. The official Postgres image was extended by adding Flask-SQLAlchemy inside the `albums-service` container.

### Run

```sh
  $ docker-compose up --build -d
```
The web service runs on port 9000.

### Tests

```sh
  $ docker exec -it albums-service bash
```
Inside the container run:
```sh
  $ python manage.py test
```
