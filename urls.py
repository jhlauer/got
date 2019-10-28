from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/2.1/topics/http/urls/
app_name='got'
urlpatterns = [
    #character
    path('', views.MainView.as_view(), name='all'),
    path('main/create/', views.CharacterCreate.as_view(), name='character_create'),
    path('main/<int:pk>/update/', views.CharacterUpdate.as_view(), name='character_update'),
    path('main/<int:pk>/delete/', views.CharacterDelete.as_view(), name='character_delete'),
    #house
    path('lookup/', views.HouseView.as_view(), name='house_list'),
    path('lookup/create/', views.HouseCreate.as_view(), name='house_create'),
    path('lookup/<int:pk>/update/', views.HouseUpdate.as_view(), name='house_update'),
    path('lookup/<int:pk>/delete/', views.HouseDelete.as_view(), name='house_delete'),
    #culture
    path('lookup/', views.CultureView.as_view(), name='culture_list'),
    path('lookup/create/', views.CultureCreate.as_view(), name='culture_create'),
    path('lookup/<int:pk>/update/', views.CultureUpdate.as_view(), name='culture_update'),
    path('lookup/<int:pk>/delete/', views.CultureDelete.as_view(), name='culture_delete'),
    #title
    path('lookup/', views.TitleView.as_view(), name='title_list'),
    path('lookup/create/', views.TitleCreate.as_view(), name='title_create'),
    path('lookup/<int:pk>/update/', views.TitleUpdate.as_view(), name='title_update'),
    path('lookup/<int:pk>/delete/', views.TitleDelete.as_view(), name='title_delete'),
]
