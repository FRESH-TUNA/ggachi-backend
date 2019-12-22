FROM        django_base
MAINTAINER  lunacircle4@gmail.com

COPY    ./requirements.txt /app/web/requirements.txt
RUN     pyenv virtualenv 3.6.4 ggachi
RUN     /root/.pyenv/versions/ggachi/bin/pip install --upgrade pip
RUN     /root/.pyenv/versions/ggachi/bin/pip install -r /app/web/requirements.txt 