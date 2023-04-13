from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

from .models import Publication, Article


def index(req, id):
    publication = Publication.objects.get(id=id)

    result = publication.article_set.all()

    return HttpResponse(result)


def create(req):
    article_1 = Article(headline='Article 1')
    article_1.save()

    article_2 = Article(headline='Article 2')
    article_2.save()

    publication_1 = Publication(title='Publication 1')
    publication_1.save()

    publication_2 = Publication(title='Publication 2')
    publication_2.save()

    article_1.publications.add(publication_1)
    article_1.publications.add(publication_2)

    article_2.publications.add(publication_1)
    article_2.publications.add(publication_2)

    result = article_1.publications.all()

    return HttpResponse(result)
