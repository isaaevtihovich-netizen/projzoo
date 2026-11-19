from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import *

def index(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def contacts_view(request):
    return render(request, 'contacts.html')

def how_to_find_view(request):
    return render(request, 'how_to_find_us.html')

def animals_view(request):
    return render(request, 'animals.html')

class AnimalsListView(ListView):
    model = Animals
    template_name = 'animals/animals_list.html'
    context_object_name = 'animals'
class AnimalsDetailView(DetailView):
    model = Animals
    template_name = 'animals/animals_detail.html'
    context_object_name = 'animal'

class AnimalsCreateView(CreateView):
    model = Animals
    form_class = AnimalsForm
    template_name = 'animals/animals_form.html'
    success_url = reverse_lazy('animals_list')

class AnimalsUpdateView(UpdateView):
    model = Animals
    form_class = AnimalsForm
    template_name = 'animals/animals_form.html'
    success_url = reverse_lazy('animals_list')

class AnimalsDeleteView(DeleteView):
    model = Animals
    template_name = 'animals/animals_confirm_delete.html'
    success_url = reverse_lazy('animals_list')

class VidListView(ListView):
    model = Vid
    template_name = 'vid/vid_list.html'
    context_object_name = 'vids'

class VidDetailView(DetailView):
    model = Vid
    template_name = 'vid/vid_detail.html'
    context_object_name = 'vid'

class VidCreateView(CreateView):
    model = Vid
    form_class = VidForm
    template_name = 'vid/vid_form.html'
    success_url = reverse_lazy('vid_list')

class VidUpdateView(UpdateView):
    model = Vid
    form_class = VidForm
    template_name = 'vid/vid_form.html'
    success_url = reverse_lazy('vid_list')

class VidDeleteView(DeleteView):
    model = Vid
    template_name = 'vid/vid_confirm_delete.html'
    success_url = reverse_lazy('vid_list')

class TipListView(ListView):
    model = Tip
    template_name = 'tip/tip_list.html'
    context_object_name = 'tips'

class TipDetailView(DetailView):
    model = Tip
    template_name = 'tip/tip_detail.html'
    context_object_name = 'tip'

class TipCreateView(CreateView):
    model = Tip
    form_class = TipForm
    template_name = 'tip/tip_form.html'
    success_url = reverse_lazy('tip_list')

class TipUpdateView(UpdateView):
    model = Tip
    form_class = TipForm
    template_name = 'tip/tip_form.html'
    success_url = reverse_lazy('tip_list')
class TipDeleteView(DeleteView):
    model = Tip
    template_name = 'tip/tip_confirm_delete.html'
    success_url = reverse_lazy('tip_list')

class SotrListView(ListView):
    model = Sotr
    template_name = 'sotr/sotr_list.html'
    context_object_name = 'sotr'

class SotrDetailView(DetailView):
    model = Sotr
    template_name = 'sotr/sotr_detail.html'
    context_object_name = 'employee'

class SotrCreateView(CreateView):
    model = Sotr
    form_class = SotrForm
    template_name = 'sotr/sotr_form.html'
    success_url = reverse_lazy('sotr_list')

class SotrUpdateView(UpdateView):
    model = Sotr
    form_class = SotrForm
    template_name = 'sotr/sotr_form.html'
    success_url = reverse_lazy('sotr_list')

class SotrDeleteView(DeleteView):
    model = Sotr
    template_name = 'sotr/sotr_confirm_delete.html'
    success_url = reverse_lazy('sotr_list')

class DolznostListView(ListView):
    model = Dolznost
    template_name = 'dolznost/dolznost_list.html'
    context_object_name = 'dolznosti'

class DolznostDetailView(DetailView):
    model = Dolznost
    template_name = 'dolznost/dolznost_detail.html'
    context_object_name = 'dolznost'

class DolznostCreateView(CreateView):
    model = Dolznost
    form_class = DolznostForm
    template_name = 'dolznost/dolznost_form.html'
    success_url = reverse_lazy('dolznost_list')

class DolznostUpdateView(UpdateView):
    model = Dolznost
    form_class = DolznostForm
    template_name = 'dolznost/dolznost_form.html'
    success_url = reverse_lazy('dolznost_list')

class DolznostDeleteView(DeleteView):
    model = Dolznost
    template_name = 'dolznost/dolznost_confirm_delete.html'
    success_url = reverse_lazy('dolznost_list')
