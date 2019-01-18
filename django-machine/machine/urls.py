from django.urls import path
from . import views

app_name = 'machine'
urlpatterns = [
    path('', views.index, name='index'),
    path('import_defaul/', views.import_defult_value, name='import_defult_value'),
    path('detail/', views.detail_view, name='detail'),
]
