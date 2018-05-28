#!/bin/bash


if [ ! -z "$NGINX_SSL_DIR" ]; then
    if [ ! -d "$NGINX_SSL_DIR" ]; then
        echo "Waiting for ssl dir $NGINX_SSL_DIR"
        until [ -d "$NGINX_SSL_DIR" ]; do
            sleep .2
        done
    fi
fi

exec nginx -g 'daemon off;'
