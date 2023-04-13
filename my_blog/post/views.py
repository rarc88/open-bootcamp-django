from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict

from .models import Author


def index(req):
    authors = Author.objects.values().all().order_by('email')

    filtered = Author.objects.values().filter(email='wkim@example.org')

    filtered = Author.objects.values().filter(email__contains='@example.org')

    filtered = Author.objects.values().filter(id__gte=5, id__lte=10)

    author = Author.objects.values().get(id=1)

    limit = Author.objects.values().all()[:10]

    offset = Author.objects.values().all()[5:15]

    context = {'authors': list(authors), 'filtered': list(filtered),
               'author': author, 'limit': list(limit), 'offset': list(offset)}

    return render(req, 'post/index.html', context)
    # return JsonResponse(context, safe=False)


def update(req, id):
    author = Author.objects.get(id=id)
    author.name = 'Roberto Ruiz'
    author.email = 'rarc88@gmail.com'
    author.save()

    return JsonResponse(model_to_dict(author))
