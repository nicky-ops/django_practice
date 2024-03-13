from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from django.contrib.flatpages.models import FlatPage
from django.shortcuts import render_to_response
# Create your views here.

def search(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = FlatPage.objects.filter(content__icontains=query)
    return render_to_response('search/search.html', {'query': query,
                                                     'results': results})

