from django.shortcuts import render
from .models import Entry

# Create your views here.
def entries_index(request):
    return render(request, "entry_index.html", {
        "entry_list": Entry.objects.all(),
    })

def entry_detail(request, year, month, day, slug):
    import datetime, time
    date_stamp = time.strptime(year+month+day, '%Y%b%d')
    pub_date = datetime.date(*date_stamp[:3])
    return render('entry_detail.html',
                              {
                                  'entry': Entry.objects.get(pub_date_year=pub_date.year,
                                                             pub_date_month=pub_date.month,
                                                             pub_date_day=pub_date.day,
                                                             slug=slug)
                              })