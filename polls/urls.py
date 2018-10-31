from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('results/<int:question_number>/', views.results, name='results'),
    path('checkList/<int:check_number>/', views.checkList, name = 'checkList'),
    path('allResults/', views.allResults, name = 'allResults')
]