from django.contrib import admin
from django.urls import path, include
from hw_project.quotes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("quotes.urls")),
    path('users/', include('users.urls')),
    path('author/<str:author_id>/', views.author_detail, name='author_detail'),

    # path("users/", include("users.urls"))
]
