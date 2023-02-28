from django.urls import path
from. import views

urlpatterns = [
    path('pedegoiaba', views.index, name='index'),
    path('<str:nome>', views.saudacao, name='saudacao' )
]
