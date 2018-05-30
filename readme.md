# Photo Album

## Flask-React-Docker Microservices App

### Summary

This is a responsive web app where users can create personal image galleries.

The app is powered by Flask REST API, React.js and PostgreSQL, which run in separate containers as microservices, brought up by Docker Compose. Image sliders and the rest of the user interface were created from scratch in React. Login with Google (OAuth 2.0) is provided for creating private galleries.

### Demo

[Work in progress...]

### Specific Functionality

### Run

```sh
  $ docker-compose up --build -d
```
The web service runs on port 9000.

### Tests

```sh
  $ docker exec -it albums-service bash
  $ python manage.py test
```
