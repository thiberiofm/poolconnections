FROM python:3.7.4-alpine3.10
MAINTAINER Thiberio F Menezes <thiberio.freitas@gmail.com>
# Packages that we need 
WORKDIR /
# instruction to be run during image build
RUN pip3 install mysql-connector-python
# Copy all the files from current source duirectory(from your system) to
# Docker container in /app directory 
COPY  ./app/app.py /
#ENTRYPOINT [“python”]
# We want to start app.py file.
# Argument to python command initialize the app
CMD ["python", "./app.py"]