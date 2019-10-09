# Python connection pool


This is a simple connection pool app in Python with mysql.

For a real connection pool I would recommend an Architecure with a Load Balancer, a connection pool app and a database cluster to write and read the requests from the client with all monitoring and logging layers.

## Installation

- Python 3.7.4
- MySQL 5 >

## Python modules

- mysql.connector

```sh
$ pip3 install mysql-connector 
```
## Run

- Install and start MySQL on LocalHost.
- Install Python 3.
-  Run app.py.

# Resources

Dillinger uses a number of open source projects to work properly:

* [MySQL - Pool Connection](https://dev.mysql.com/doc/connector-python/en/connector-python-connection-pooling.html) - Developer portal from Oracle
* [The C10K problem](http://www.kegel.com/c10k.html) - "How to handle with thounsads of connections" 
