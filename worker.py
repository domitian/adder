import redis
import time
r = redis.Redis()
REDIS_QUEUE = 'input_queue'

def parse_input(response):
    print response
    print response.split(":")
    return response.split(":")

while 1:
    try:
        response = r.blpop(REDIS_QUEUE)
        a,b,unique_id = parse_input(response[1])
        total = int(a) + int(b)
        r.set(unique_id,total)
    except redis.exceptions.ConnectionError:
        print "Connection Lost,Trying to connect again in 5 seconds"
        time.sleep(5)

    
    
