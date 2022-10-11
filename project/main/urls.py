from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('test_detail/<int:id>/', category_detail, name='test_detail')
]
