FROM python:3.7-slim-buster

RUN apt-get update && \
 apt-get install --no-install-recommends -y python3.7-dev build-essential zlib1g-dev gcc && \
 rm -rf /var/lib/apt/lists/*

ENV LOG_LEVEL INFO
ENV PYTHONPATH /app
ENV HOST '0.0.0.0'
ENV PORT 5000

WORKDIR /app
ARG NO_CACHE=1
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

CMD ["python", "bot.py"]