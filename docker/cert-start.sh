#!/usr/bin/env bash

POSTGRES_CERTIFICATES_PATH=/.postgresql

if [ "$POSTGRES_ENABLE_SSL_AUTH" = "true" ]
then
  cp $POSTGRES_CERTS_MOUNT_PATH/* $POSTGRES_CERTIFICATES_PATH/
  chmod 400 $POSTGRES_CERTIFICATES_PATH/$POSTGRES_CERT_FILE_NAME
  chmod 400 $POSTGRES_CERTIFICATES_PATH/$POSTGRES_KEY_FILE_NAME
fi

python3 /usr/local/bin/entrypoint.py