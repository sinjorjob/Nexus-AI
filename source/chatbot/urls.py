from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_view, name='chat'),
    path('chat/', views.chat_view, name='chat_api'),
    path('update-instructions/', views.update_instructions, name='update_instructions'),
    path('update-instructions-view/', views.update_instructions_view, name='update_instructions-view'),
]