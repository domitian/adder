#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Job
import redis
r = redis.Redis()
REDIS_QUEUE = 'input_queue'

def index(request):
    inp1 = request.GET.get('inp1')
    inp2 = request.GET.get('inp2')
    job_id = None
    if inp1 is None or inp2 is None:
        output = "Please pass inputs"
    else:
        try:
            inp = inp1 + ":" + inp2
            j = Job(inp=inp)
            j.save()
# Push the data to redis for processing by workers
            redis_list = str(inp + ":" + str(j.id))
            r.rpush(REDIS_QUEUE,redis_list)
            job_id = str(j.id) 
            output = "inputs passed are " + inp1 + " and " + inp2 
        except redis.exceptions.ConnectionError:
            output = "Looks like redis server is down, please try again later"
    template = loader.get_template("poller/index.html")
    context = {
            'output': output,
	    'job_id': job_id
            }
    return HttpResponse(template.render(context, request))

def results(request,job_id):
    try:
        result = Job.objects.filter(id=job_id)
        if len(result) == 0 :
            output = "Invalid Job Id"
        else:
            result = result[0]
            if result.status == Job.QUEUED:
                data = r.get(job_id)
                r.delete([job_id])
                if data is None:
                    output = "Job is Still Queued"
                else:
                    result.status = Job.FINISHED
                    result.result = data
                    result.save()
            output = "<p>Job is Finished, the sum is " + result.result+"</p><p><a href=/poller/>Give more Inputs</a></p>"
    except redis.exceptions.ConnectionError:
        output = "Looks like redis server is down, please try again later"
    return HttpResponse(output)
