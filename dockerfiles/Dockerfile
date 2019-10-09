FROM python:3.7.4-alpine3.10
MAINTAINER Thiberio F Menezes <thiberio.freitas@gmail.com>
# Packages that we need 
WORKDIR /app
# instruction to be run during image build
RUN pip3 install mysql-connector-python
# Copy all the files from current source duirectory(from your system) to
# Docker container in /app directory 
COPY /app/ app.py
# Specifies a command that will always be executed when the  
# container starts.
# In this case we want to start the python interpreter
ENTRYPOINT [“python”]
# We want to start app.py file. (change it with your file name) 
# Argument to python command
CMD [“app.py”]