from django.shortcuts import render
from django.http import HttpResponse

from .forms import CommentForm, ContactForm


def form(req):
    comment_form = CommentForm()
    return render(req, 'form.html', {'comment_form': comment_form})


def goal(req):
    if req.method != 'POST':
        return HttpResponse('This endpoint only support the method POST')

    name = req.POST['name']
    return render(req, 'success.html', {'name': name})


def widget(req):
    if req.method == 'GET':
        contact_form = ContactForm()
        return render(req, 'widget.html', {'contact_form': contact_form})
    if req.method == 'POST':
        contact_form = ContactForm(req.POST)
        if contact_form.is_valid():
            return HttpResponse('The form is valid')
        else:
            return render(req, 'widget.html', {'contact_form': contact_form})

    return HttpResponse('This endpoint only support the methods GET or POST')
