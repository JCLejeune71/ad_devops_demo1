#!/bin/sh
set -e
sed -i "s|__FE_VERSION__|${APP_VERSION:-v1.0}|g" /usr/share/nginx/html/index.html
sed -i "s|__FE_DEPLOYED_BY__|${DEPLOYED_BY:-manual}|g" /usr/share/nginx/html/index.html
exec nginx -g "daemon off;"
