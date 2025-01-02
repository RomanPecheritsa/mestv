from django.urls import path

from houses.apps import HousesConfig
from houses.views import HomePageView

app_name = HousesConfig.name

urlpatterns = [path("", HomePageView.as_view(), name="home")]
