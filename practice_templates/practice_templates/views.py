from django.shortcuts import render


def index(req):
    return render(req, 'index.html', {})


def portfolio(req):
    return render(req, 'portfolio.html', {})
