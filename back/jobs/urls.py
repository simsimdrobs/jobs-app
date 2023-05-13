from django.urls import path
from .views import *

urlpatterns = [
	path('', name='all', view=get)
]
