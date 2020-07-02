# Json API Consumer example
## Introduction

This is a simple example about how to consume an API using Python.

*[jsonplaceholder.py](/jsonplaceholder.py)* module consumes the API from [JSONPlaceholder](https://jsonplaceholder.typicode.com/) using httplib and basic OOP implementation.

*[consumer.py](/consumer.py)* is a simple consumer and works as a wrapper to consume Json Place Holder API. It opens a socket on port 80 in your local machine and receives HTTP requests from your local browser.

## Requirements

Python3

## How To

```
pip3 install -r requirements.txt
python3 consumer.py
```

You will see the following output:

![Alt text](images/console.png?raw=true)

Open your browser and enter ```localhost/users/1``` ( *1* is the *user id* to query and consume the API from [JSONPlaceholder](https://jsonplaceholder.typicode.com/ ).
You will see a JSON output with all the records for this user.

![Alt text](images/browser.png?raw=true)
