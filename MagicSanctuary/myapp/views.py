from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Keeper
from .Keeper_forms import Keeper


class KeeperListView(ListView):
    model = Keeper
    template_name = 'myapp/keeper_list.html'
    context_object_name = 'keepers'

class KeeperDetailView(DetailView):
    model = Keeper
    template_name = 'myapp/keeper_detail.html'
    context_object_name = 'keeper'

class KeeperCreateView(CreateView):
    model = Keeper
    template_name = 'myapp/keeper_form.html'
    success_url = reverse_lazy('myapp:keeper_form')
    form_class = KeeperForm




