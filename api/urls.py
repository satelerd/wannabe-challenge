from django.urls import path
from .views import AirportListView
from .views import AirlineListView
from .views import FlightListView
    
urlpatterns = [
    path("airport", AirportListView.as_view()),
    path("airline", AirlineListView.as_view()),
    path("flight", FlightListView.as_view()),
]