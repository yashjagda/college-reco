from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView,DetailView
from colleges.models  import CollegeDetails,Location, Caste,Field
# Create your views here.
def index(request):
    colleges = CollegeDetails.objects.filter(rating__gte="4")[:6]
    location = Location.objects.all()[:7]
    casteform = Caste.objects.all()[:7]
    fieldform = Field.objects.all()[:7]
    context = {
    'colleges': colleges,
    'location': location,
    'caste': casteform,
    'field': fieldform
    }
    return render(request, 'landing/index.html',context)

def about(request):
    return render(request, 'landing/about.html')

def downloads(request):
    return render(request, 'colleges/download.html')

class CollegeDetailView(DetailView):
        model = CollegeDetails
        context_object_name = 'college_detail'
        template_name = 'landing/college.html'
