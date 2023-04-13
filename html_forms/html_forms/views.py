from django.shortcuts import render
from django.http import HttpResponse


def getForm(req):
    return render(req, 'get_form.html', {})


def getGoal(req):
    if req.method != 'GET':
        return HttpResponse('This endpoint only support the method GET')

    name = req.GET['name']
    return render(req, 'get_success.html', {'name': name})


def postForm(req):
    return render(req, 'post_form.html', {})


def postGoal(req):
    if req.method != 'POST':
        return HttpResponse('This endpoint only support the method POST')

    name = req.POST['name']
    return render(req, 'post_success.html', {'name': name})
