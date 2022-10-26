#!/bin/bash

echo "Flushing manage" > docker_ini.log

while ! python manage.py flush --no-input 2>&1; do
  echo "Flusing django manage command" >> docker_ini.log
  sleep 3
done

echo "Doing database migration" >> docker_ini.log
# Wait for few minute and run db migraiton
while ! python manage.py migrate  2>&1; do
   echo "Executing migrations" >> docker_ini.log
   sleep 3
done

echo "Creating superuser" >> docker_ini.log
python manage.py createsuperuser \
    --noinput \
    --username $DJANGO_SUPERUSER_USERNAME \
    --email $DJANGO_SUPERUSER_EMAIL
echo " -> Superuser was created in database!" >> docker_ini.log

echo "Documanager app configured successfully." >> docker_ini.log

exec "$@"
