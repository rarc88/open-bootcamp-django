from django.shortcuts import render


def statics(req):
    return render(req, 'statics.html', {})
