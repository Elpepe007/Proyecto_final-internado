from django.urls import path
from App_1 import views

urlpatterns = [
    path('index/', views.ver_template_index, name='index'),
    path('internos/', views.ver_template_internos, name='internos'),
    path('jefes/', views.ver_template_jefes, name='jefes'),
    path('maestros/', views.ver_template_maestros, name='maestros'),
    path('preceptores/', views.ver_template_preceptores, name='preceptores'), 
 
] 