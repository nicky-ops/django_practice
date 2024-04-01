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

class ArchiveIndexView(DetailView):
    model = Entry
    template_name = 'archive_index.html'
    context_object_name = 'entry'
    date_field = 'pub_date'
    month_format = '%b'
    allow_empty = True



class YearArchiveView(DetailView):
    model = Entry
    template_name = 'archive_year.html'
    context_object_name = 'entry'
    date_field = 'pub_date'
    month_format = '%b'
    make_object_list = True
    allow_empty = True

class MonthArchiveView(DetailView):
    model = Entry
    template_name = 'archive_month.html'
    context_object_name = 'entry'
    date_field = 'pub_date'
    month_format = '%b'
    allow_empty = True

class DayArchiveView(DetailView):
    model = Entry
    template_name = 'archive_day.html'
    context_object_name = 'entry'
    date_field = 'pub_date'
    month_format = '%b'
    allow_empty = True


class DateDetailView(DetailView):
    model = Entry
    template_name = 'entry_detail.html'
    context_object_name = 'entry'
    slug_field = 'slug'
    month_format = '%b'
    date_field = 'pub_date'
    query_pk_and_slug = True
