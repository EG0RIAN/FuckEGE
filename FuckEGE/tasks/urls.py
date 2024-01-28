from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.download_csv, name='download_csv'),
    path('get_json/', views.json_answers, name='json_answers'),
    path('', views.index, name='index'),
    path('api/message/', views.post_message, name='post_message'),
]


admin.site.site_header = "Ебал информатичку"
admin.site.site_title = "Ебал информатичку"
admin.site.index_title = "Ебал информатичку"
