from django.urls import path
from .views import AirportListView

urlpatterns = [
    path("airport", AirportListView.as_view()),
]