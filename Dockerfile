FROM python:3.8-alpine3.11


ENV PYTHONDONTWRITEBYTECODE 1

COPY src /app

COPY requirements.txt /app

WORKDIR /app

RUN pip3 install -r requirements.txt \
    && rm -f /app/requirements.txt

ENTRYPOINT ["python3"]

CMD ["financer.py"]
