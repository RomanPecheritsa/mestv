from django.views import generic
from django.views.generic import TemplateView

from houses.models import House


class HomePageView(TemplateView):
    template_name = "main.html"


class HouseListView(generic.ListView):
    model = House
    queryset = House.objects.all()


class HouseDetailView(generic.DetailView):
    model = House
    queryset = House.objects.all()
