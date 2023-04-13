from django.shortcuts import render


def index(req):
    return render(req, 'index.html', {})


def option1(req):
    return render(req, 'option1.html', {})


def option2(req):
    return render(req, 'option2.html', {})
