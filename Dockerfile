FROM python:3.6.1

RUN apt-get update -yqq \
  && apt-get install -yqq --no-install-recommends \
    netcat \
  && apt-get -q clean

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

ADD ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

ADD . /usr/src/app

RUN chmod +x entrypoint.sh

CMD ["./entrypoint.sh"]
