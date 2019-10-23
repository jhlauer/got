from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/2.1/topics/http/urls/
app_name='APPNAME'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('main/create/', views.Model_2Create.as_view(), name='model_2_create'),
    path('main/<int:pk>/update/', views.Model_2Update.as_view(), name='model_2_update'),
    path('main/<int:pk>/delete/', views.Model_2Delete.as_view(), name='model_2_delete'),
    path('lookup/', views.Model_1View.as_view(), name='model_1_list'),
    path('lookup/create/', views.Model_1Create.as_view(), name='model_1_create'),
    path('lookup/<int:pk>/update/', views.Model_1Update.as_view(), name='model_1_update'),
    path('lookup/<int:pk>/delete/', views.Model_1Delete.as_view(), name='model_1_delete'),
]
