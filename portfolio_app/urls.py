from django.urls import path
from . import views

urlpatterns = [
    path('' ,views.home , name="home"),
    path('compose_email/' , views.compose_email , name='compose_email'),
]
