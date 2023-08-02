from django.urls import path

from . import views

app_name = "quotes"

urlpatterns = [
    path('', views.main, name="root"),
    path('paginate/<int:page>/', views.main, name="root_paginate"),
    # path('', include('users.urls')),
    path('author/<str:id>/', views.author_detail, name='author_detail'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('add_author/', views.add_author, name='add_author'),
    path('first_page/', views.first_page, name='first_page'),
    path('last_page/', views.last_page, name='last_page'),

]