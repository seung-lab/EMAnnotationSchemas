FROM tiangolo/uwsgi-nginx-flask:python3.11

ENV UWSGI_INI ./uwsgi.ini
RUN python -m pip install --upgrade pip

RUN mkdir -p /home/nginx/.cloudvolume/secrets && chown -R nginx /home/nginx && usermod -d /home/nginx -s /bin/bash nginx

COPY requirements.txt /app/.
COPY requirements_service.txt /app/.

RUN pip install numpy && \
    pip install -r requirements.txt && \
    pip install -r requirements_service.txt
COPY . /app
