from django.urls import path
from .views import AirportListView
from .views import AirlineListView

urlpatterns = [
    path("airport", AirportListView.as_view()),
    path("airline", AirlineListView.as_view()),
]