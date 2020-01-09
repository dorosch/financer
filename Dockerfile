FROM python:3.8-alpine3.11


ENV PYTHONDONTWRITEBYTECODE 1

COPY src /app

COPY requirements.txt /tmp

WORKDIR /app

RUN pip3 install -r /tmp/requirements.txt && \
    rm -f /tmp/requirements.txt

ENTRYPOINT ["sh"]
