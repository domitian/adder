#### Prerequisites:

1. Python version 2.7.6
2. Django Version 1.9.3
3. Redis Server has to be installed, and redis python client also has to be installed as well.
4. Python redis client used is *redis-py*. To install the client run `pip install redis`.
5. Database used - sqlite3

#### Info:

This project is divided into two parts, 

1. Webapp - Django web application frontend which provides the UI to provide inputs.
2. worker - which is a simple script worker.py

To change redis settings for webapp, change it in settings.py for the django app.
To change worker redis settings open worker.py, where it has a constant name **REDIS_HOST** and **REDIS_PORT**.

### Worker:

Worker connects to the redis server and polls it for any job using BLPOP functionality of redis queue.
If any job is in the queue defined by this constant REDIS_INPUT_QUEUE, it processes input and pushes the results back to redis server by setting the unique id it got as input as key and result as the value.

To run the worker, run this command
` python worker.py`

### Webapp:

Django application resides in webapp folder, the app resides in *poller* folder inside django application folder.
To run the app
`django manage.py runserver`

When initial input is given, the input data is stored in job table of the database and inputs and id of the job is pushed to redis queue.
When request is made to fetch the result, if the result is not in database, it polls the redis server by the job id and shows the result and stores it in database as well. 

###### Workflow:

To give input numbers as sum, go to this [url](localhost:8000/poller)
Provide the input and query the server again for result using the link provided after submitting the job to process.

### Possible Improvements:

We can use another background processor for django webapp to poll the redis server for results and store them in database, so we don't have to call redis server while the user asks for the status of the job.
