from django.urls import path

from houses.views import HomePageView, HouseDetailView, HouseListView

app_name = "houses"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("houses/", HouseListView.as_view(), name="house_list"),
    path("houses/<int:pk>/", HouseDetailView.as_view(), name="house_detail"),
]
