from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('liste', views.liste),
    path('detay', views.detay),
    path('kategori/<int:id>', views.getCoursesById),
    path('kategori/<str:eld>', views.getCoursesByCategory, name='courses_by_category'),
]