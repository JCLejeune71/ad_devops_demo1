FROM nginx:alpine

COPY index.html /usr/share/nginx/html/index.html
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENV APP_VERSION="v1.0"
ENV DEPLOYED_BY="manual"

CMD ["/entrypoint.sh"]
