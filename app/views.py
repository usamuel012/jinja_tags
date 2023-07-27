from django.shortcuts import render

# Create your views here.

def jinja(request):
    j = {'name': 'Ethan Hunt', 'age': 19}
    return render(request, 'jinja.html', context=j)
