from . import views
from django.urls import path,include

urlpatterns = [

    path('',views.index,name='home'),
    path('fullforms/',views.fullform,name='fullform'),
    path('feedback/',views.feedback,name='feedback'),
]
