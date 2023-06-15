from django.urls import path,include
from . import views


urlpatterns = [
    path("",views.fontgen,name="fontgen"),
    path("newcard",views.cardgen,name="newcard"),
]