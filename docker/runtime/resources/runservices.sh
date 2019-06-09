#!/bin/bash

# for development mode
if [[ ${DEVELOPMENT} ]]; then
    source $VENV_DIR/bin/activate
    echo "Development mode was enabled, this mode use virtualenv"
fi

gunicorn -c /resources/gunicorn.py wsgi:app
