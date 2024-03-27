from django.shortcuts import render, get_object_or_404
from .models import Entry
from django.views.generic import DetailView

# Create your views here.
def entries_index(request):
    return render(request, "entry_index.html", {
        "entry_list": Entry.objects.all(),
    })

class EntryDetailView(DetailView):
    model = Entry
    template_name = 'entry_detail.html'
    context_object_name = 'entry'
    slug_field = 'slug'
    month_format = '%b'
    date_field = 'pub_date'
    query_pk_and_slug = True