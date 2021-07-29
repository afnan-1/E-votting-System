from django.urls import path
from .views import *

urlpatterns = [
    path('getsocities/',get_all_societies),
    path('society/<int:id>/',get_society),
    path('candidate/',add_vote),
    path('results/',get_result)
]
