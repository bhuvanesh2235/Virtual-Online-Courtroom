from django.urls import path
from .views import CaseListCreate, home

urlpatterns = [
    path('cases/', CaseListCreate.as_view(), name='case-list-create'),
    path('', home, name='home'),  # Add root URL pattern
]
