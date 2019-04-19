from django.urls import path
from . import views
app_name = 'college'
urlpatterns = [
    path('', views.index, name= 'colleges' ),
    path('predict', views.listing, name= 'listing' ),
    path('<int:pk>/',views.CollegeDetailView.as_view(),name='detail')
    #path('<slug:slug>/', views.CollegeDetailView.as_view(), name='detail'),
]
