#!/bin/bash

# SSL connection for postgres
POSTGRES_CERTIFICATES_PATH=/.postgresql

if [ "$POSTGRES_ENABLE_SSL_AUTH" = "true" ]
then
  cp $POSTGRES_CERTS_MOUNT_PATH/* $POSTGRES_CERTIFICATES_PATH/
  chmod 400 $POSTGRES_CERTIFICATES_PATH/$POSTGRES_CERT_FILE_NAME
  chmod 400 $POSTGRES_CERTIFICATES_PATH/$POSTGRES_KEY_FILE_NAME
fi


# Check if uwsgi configuration exists
if [[ ! -f /settings/uwsgi.ini ]]; then
  echo "/settings/uwsgi.ini doesn't exists"
  # If it doesn't exists, copy from /pycsw directory if exists
  if [[ -f /pycsw/uwsgi.ini ]]; then
    cp -f /pycsw/uwsgi.ini /settings/uwsgi.ini
  else
    # default value
    envsubst </settings/uwsgi.default.ini >/settings/uwsgi.ini
  fi
fi

#su $USER_NAME -c "uwsgi --ini /uwsgi.conf"
sed -i -e "s/uid = 1000/uid = $(id -u)/g" /settings/uwsgi.ini
exec uwsgi --ini /settings/uwsgi.ini
