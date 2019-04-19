from django.urls import path
from . import views

app_name = 'landing'
urlpatterns = [
    path('', views.index, name= 'index' ),
    path('downloads', views.downloads, name='downloads'),
    path('about', views.about, name='about'),
    path('<int:pk>/',views.CollegeDetailView.as_view(),name='detail')
]
