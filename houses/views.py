from django.views import generic
from django.views.generic import TemplateView

from houses.models import ContactInfo, HeaderText, House


class HomePageView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data["header_texts"] = HeaderText.objects.all()
        data["header_button_text"] = "Наши дома"
        data["title"] = "Moscow Estate - загородные дома под ключ возле Москвы"
        data["contact_info"] = ContactInfo.objects.first()
        return data


class ComponentsPageView(TemplateView):
    template_name = "components.html"


class HouseListView(generic.ListView):
    model = House
    queryset = House.objects.all()
    context_object_name = "houses"

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        houses_with_main_photo = []
        for house in data["houses"]:
            main_photo = house.photos.filter(is_main=True).first()
            houses_with_main_photo.append({"house": house, "main_photo": main_photo})
        data["houses_with_main_photo"] = houses_with_main_photo

        return data


#
#
# class HouseDetailView(generic.DetailView):
#     model = House
#     queryset = House.objects.all()
#     context_object_name = 'house'
