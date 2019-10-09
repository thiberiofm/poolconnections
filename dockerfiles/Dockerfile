FROM python:3.7.4-alpine3.10
MAINTAINER Thiberio F Menezes <thiberio.freitas@gmail.com>

ADD app/ /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt \
    && pip3 install mysql-connector-python

EXPOSE 5000

ENV app.py
ENTRYPOINT ["python", "-m", "run", "--host=0.0.0.0"]
CMD ["app.py"]