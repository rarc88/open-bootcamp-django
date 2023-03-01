from django.http import HttpResponse


def greeting(req):
    return HttpResponse('Hello World!')


def farewell(req):
    return HttpResponse('Good Bye!')


def getRecord(req, id):
    if id in range(0, 11):
        return HttpResponse(f'Record {id} found')
    else:
        return HttpResponse(f'Record {id} not found')
