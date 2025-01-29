from django.shortcuts import get_object_or_404
from django.views import generic

from houses.models import ContactInfo, HeaderText, House, Interior, News


class HomePageView(generic.TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data()

        data["title"] = "Moscow Estate - загородные дома под ключ возле Москвы"

        data["header_texts"] = HeaderText.objects.all()
        data["contact_info"] = ContactInfo.objects.first()

        data["main_houses"] = House.objects.all().order_by("?")[:4]
        data["main_interiors"] = Interior.objects.all().order_by("?")[:3]
        data["main_news"] = News.objects.order_by("-created_at").first()
        return data


class ComponentsPageView(generic.TemplateView):
    template_name = "components.html"


class HouseListView(generic.ListView):
    model = House
    queryset = House.objects.all()
    context_object_name = "houses"
    paginate_by = 8


class NewsListView(generic.ListView):
    model = News
    queryset = News.objects.all()
    context_object_name = "news_list"
    paginate_by = 6


class HouseDetailView(generic.DetailView):
    model = House
    queryset = House.objects.all()
    context_object_name = "house"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        house = self.get_object()
        if house.album:
            context["photos"] = house.album.photos.all()
        else:
            context["photos"] = []
        return context


class InteriorGalleryView(generic.ListView):
    model = Interior
    template_name = "houses/interior_gallery.html"
    context_object_name = "interiors"

    def get_queryset(self):
        return Interior.objects.all().order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        interior_id = self.request.GET.get("interior")

        if interior_id:
            active_interior = get_object_or_404(Interior, id=interior_id)
        else:
            active_interior = Interior.objects.first()

        context["active_interior"] = active_interior
        context["photos"] = (
            active_interior.album.photos.all() if active_interior.album else []
        )
        return context
