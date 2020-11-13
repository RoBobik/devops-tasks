#!/bin/bash -x

# Ugly hack to give database some time to initialize
sleep 5

# Run database migrations
python clinic/manage.py migrate --noinput || exit 1

exec "$@"
