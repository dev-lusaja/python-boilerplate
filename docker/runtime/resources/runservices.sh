#!/bin/bash
source $VENV_DIR/bin/activate
gunicorn -c /resources/gunicorn.py wsgi:app