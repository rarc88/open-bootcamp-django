from django.shortcuts import render


def simple(req):
    return render(req, 'simple.html', {})


def dynamic(req, name):
    context = {'name': name, 'categories': [
        'JavaScript', 'Java', 'PHP', 'Python', 'Dart', 'sql']}
    return render(req, 'dynamic.html', context)
