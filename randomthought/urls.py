from django.urls import path

from randomthought import views

app_name = 'randomthought'

urlpatterns = [
    path('random/', views.random, name='random')
]
