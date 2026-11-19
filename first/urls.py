from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about_view, name='about'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('how_to_find/', views.how_to_find_view, name='how_to_find'),
    path('animals/', views.animals_view, name='animals'),

    path('animals/list/', views.AnimalsListView.as_view(), name='animals_list'),
    path('animals/<int:pk>/', views.AnimalsDetailView.as_view(), name='animals_detail'),
    path('animals/create/', views.AnimalsCreateView.as_view(), name='animals_create'),
    path('animals/<int:pk>/update/', views.AnimalsUpdateView.as_view(), name='animals_update'),
    path('animals/<int:pk>/delete/', views.AnimalsDeleteView.as_view(), name='animals_delete'),

    path('vid/', views.VidListView.as_view(), name='vid_list'),
    path('vid/<int:pk>/', views.VidDetailView.as_view(), name='vid_detail'),
    path('vid/create/', views.VidCreateView.as_view(), name='vid_create'),
    path('vid/<int:pk>/update/', views.VidUpdateView.as_view(), name='vid_update'),
    path('vid/<int:pk>/delete/', views.VidDeleteView.as_view(), name='vid_delete'),

    path('tip/', views.TipListView.as_view(), name='tip_list'),
    path('tip/<int:pk>/', views.TipDetailView.as_view(), name='tip_detail'),
    path('tip/create/', views.TipCreateView.as_view(), name='tip_create'),
    path('tip/<int:pk>/update/', views.TipUpdateView.as_view(), name='tip_update'),
    path('tip/<int:pk>/delete/', views.TipDeleteView.as_view(), name='tip_delete'),

    path('sotr/', views.SotrListView.as_view(), name='sotr_list'),
    path('sotr/<int:pk>/', views.SotrDetailView.as_view(), name='sotr_detail'),
    path('sotr/create/', views.SotrCreateView.as_view(), name='sotr_create'),
    path('sotr/<int:pk>/update/', views.SotrUpdateView.as_view(), name='sotr_update'),
    path('sotr/<int:pk>/delete/', views.SotrDeleteView.as_view(), name='sotr_delete'),

    path('dolznost/', views.DolznostListView.as_view(), name='dolznost_list'),
    path('dolznost/<int:pk>/', views.DolznostDetailView.as_view(), name='dolznost_detail'),
    path('dolznost/create/', views.DolznostCreateView.as_view(), name='dolznost_create'),
    path('dolznost/<int:pk>/update/', views.DolznostUpdateView.as_view(), name='dolznost_update'),
    path('dolznost/<int:pk>/delete/', views.DolznostDeleteView.as_view(), name='dolznost_delete'),
]
