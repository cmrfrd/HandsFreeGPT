#!/usr/bin/env sh

# waiting for postgres
until psql --host=$CVML_HOST --username=$CVML_USER $CVML_NAME -w &>/dev/null
do
  echo "Waiting for CVML DB..."
  sleep 1
done

# migrate
alembic upgrade head
