from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.utils import timezone
from tablib import Dataset
from django.views.generic import View,TemplateView,ListView,DetailView
from .models  import *
from django.db.models import Q

def index(request):
    colleges = CollegeDetails.objects.all()
    location = Location.objects.all()[:7]
    paginator = Paginator(colleges, 15)
    page = request.GET.get('page')
    paged_colleges = paginator.get_page(page)

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            colleges = colleges.filter(name__icontains= keywords)
            paginator = Paginator(colleges, 15)
            page = request.GET.get('page')
            paged_colleges = paginator.get_page(page)
    context = {
    'colleges': paged_colleges,
    'location': location,

    }
    return render(request, 'colleges/colleges.html', context)

class CollegeDetailView(DetailView):
        model = CollegeDetails
        context_object_name = 'college_detail'
        template_name = 'colleges/college.html'

def listing(request):

    if request.method == 'POST':
        mark1 = request.POST.get('marks', None)
        caste = request.POST.get('caste', None)
        field = request.POST.get('field', None)
        location = request.POST.get('location',None)
        loc = Location.objects.all()[:7]
        casteform = Caste.objects.all()[:7]
        fieldform = Field.objects.all()[:7]

        college_list = Map.objects.filter(Q(f__field_name__iexact= field) & Q(caste__caste__iexact= caste) & Q(marks__lte= mark1) & Q(location_map__iexact= location))
        college_dict = {'colleges' : college_list, 'values': request.POST, 'location': loc, 'caste': casteform, 'field': fieldform}
        return render(request, 'colleges/lists.html', context=college_dict)

    else:
        return render(request, 'index.html')
