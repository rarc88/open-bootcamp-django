from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment


def index(req):
    comments = Comment.objects.all()
    return HttpResponse(comments)


def create(req):
    # comment = Comment(name='Roberto Ruiz', score=5, comment='First comment')
    # comment.save()
    comment = Comment.objects.create(name='Alex')
    return HttpResponse(comment)


def delete(req, id):
    # comment = Comment.objects.get(id=id)
    # comment.delete()
    comment = Comment.objects.filter(id=id).delete()
    return HttpResponse(comment)
