# Room Allocation
#### Checkpoint 1 Python
[![Coverage Status](https://coveralls.io/repos/andela-sndagi/room-allocation/badge.svg?branch=develop&service=github)](https://coveralls.io/github/andela-sndagi/room-allocation?branch=develop)
[![Build Status](https://semaphoreci.com/api/v1/projects/4ce0bec9-06db-40eb-a90e-3833134d7c6a/651500/badge.svg)](https://semaphoreci.com/stanmd/room-allocation)

This is a Room Allocation program. In this repository the building has 10 offices and 10 Living spaces, which are first of all pre-populated and then accepts an input text file with the names of those to be allocated and randomly allocates them to the offices and Living spaces. Those not allocated space are then returned.

To clone the repo ```git clone https://github.com/andela-sndagi/room-allocation.git``` in the terminal

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
