from django.urls import path

from houses.views import ComponentsPageView, HomePageView, HouseListView, HouseDetailView, InteriorGalleryView

app_name = "houses"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("dev/", ComponentsPageView.as_view(), name="dev"),
    path("houses/", HouseListView.as_view(), name="house_list"),
    path("houses/<int:pk>/", HouseDetailView.as_view(), name="house_detail"),
    path('interiors/', InteriorGalleryView.as_view(), name='interior_gallery'),
]
