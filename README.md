# Room Allocation
#### Checkpoint 1 Python
[![Build Status](https://semaphoreci.com/api/v1/stanmd/room-allocation/branches/master/badge.svg)](https://semaphoreci.com/stanmd/room-allocation)
[![Coverage Status](https://coveralls.io/repos/andela-sndagi/room-allocation/badge.svg?branch=develop&service=github)](https://coveralls.io/github/andela-sndagi/room-allocation?branch=develop)
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/192254c3314e40179b60d59b8d323579/badge.svg)](https://www.quantifiedcode.com/app/project/192254c3314e40179b60d59b8d323579)

> A Room Allocation program

In this repository the building has 10 offices and 10 Living spaces, which are first of all pre-populated and then accepts an input text file with the names of those to be allocated and randomly allocates them to the offices and Living spaces. Those not allocated space are then returned.

#### Installation and usage
RUN ```git clone https://github.com/NdagiStanley/room-allocation.git``` to clone this repo

Create a virtual environment using [virtualenv](https://virtualenv.readthedocs.org/en/latest/) or [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/) and do the following in it.

1. Install DEPENDENCIES
```pip install -r requirements.txt```
2. RUN
```$ python sample.py ```
or
```$ python sample.py 'file'``` 'file' here should be in the parent directory
3. TEST
```$ nosetests```
4. Check the COVERAGE of the tests
```coverage run tests/test_building.py``` and
```coverage report```

Copyright (c) 2016
###### [Stanley Ndagi](http://techkenyans.org/jamii/stanmd) c/o [Andela](http://andela.com)
