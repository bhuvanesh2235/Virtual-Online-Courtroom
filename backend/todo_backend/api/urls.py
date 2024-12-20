from django.urls import path
from . import views

urlpatterns = [
    path('cases/', views.CaseListCreate.as_view(), name='case-list-create'),
    # Add more URL patterns for your API endpoints here
]
