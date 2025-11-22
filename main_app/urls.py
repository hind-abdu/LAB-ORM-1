from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.show_post, name='home'),
    path('create_post/', views.create_post_view, name='create_post_view'),
]
