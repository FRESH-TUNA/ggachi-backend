FROM        lunacircle4/ggachi-backend:develop
MAINTAINER  lunacircle4@gmail.com

COPY ./ /app/web
# COPY /app/floweryroad-backend /app/floweryroad-backend

# nginx
# RUN         cp -f /app/.server/uwsgi.service /etc/systemd/system/uwsgi.service
RUN         cp -f /app/web/.server/supervisor_app.conf /etc/supervisor/conf.d/

# requirements.txt install
# RUN         /root/.pyenv/versions/floweryroad/bin/pip install -r /app/floweryroad-backend/requirements.txt