from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

from .models import Reporter, Article


def index(req):
    pass


def create(req):
    reporter = Reporter(first_name='Roberto',
                        last_name='Ruiz', email='rarc88@gmail.com')
    reporter.save()

    article_1 = Article(headline='Lorem Ipsum 1',
                        pub_date=date.today(), reporter=reporter)
    article_1.save()

    article_2 = Article(headline='Lorem Ipsum 2',
                        pub_date=date.today(), reporter=reporter)
    article_2.save()

    result = reporter.article_set.all()

    return HttpResponse(result)
