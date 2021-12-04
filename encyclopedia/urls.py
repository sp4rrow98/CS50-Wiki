from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="title"),
    path("new", views.new, name="new"),
    path("error", views.error, name="error"),
    path('wiki/<str:entry>/', views.entry, name='entry'),
    path('edit/<str:title>', views.edit, name='edit'),
    path('wiki', views.random_page, name='random_page')
]
