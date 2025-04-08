from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path("result", views.result, name="result"),
    # path('social_links', views.social_links),
    path('about/', views.about, name='about'),  
    path('contact/', views.contact, name='contact')
]
