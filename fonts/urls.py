from django.urls import path,include
from . import views


urlpatterns = [
    path("fontgen",views.fontgen,name="fontgen"),
    path("quiz",views.quiz,name="quiz")
]