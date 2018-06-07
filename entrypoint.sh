#!/bin/sh

gunicorn -b 0.0.0.0:5001 manage:app
