"""controllers"""
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import datetime
import json
def hola(request):
    now=datetime.now()
    return HttpResponse('current server time {now}'.format(now=str(now)))

def query(request):
    array_str= request.GET['numbers'].split(',')
    array_int=[int(i)for i in array_str]
    final={
        'status':'ok',
        'sorted_nums': sorted(array_int)
    }
    return JsonResponse(final)


def params(request,name,age):
    if age<12:
        message='Sorry {}, you are not allow here'.format(name)
    else:
        message='welcome {}'.format(name)    
    return HttpResponse(message)
        