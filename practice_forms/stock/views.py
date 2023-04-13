from django.shortcuts import render
from django.http import HttpResponse

from .forms import ProductForm


def index(req):
    if req.method == 'POST':
        form = ProductForm(req.POST)

        if form.is_valid():
            form.save()
            return render(req, 'index.html', {'form': form})

        return HttpResponse('Data not valid')
    else:
        form = ProductForm()
        return render(req, 'index.html', {'form': form})
