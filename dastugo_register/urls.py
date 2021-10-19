from django.urls import path
from .views import home
from .views import home, student_list_view, student_add_view, student_detail_view, student_update_view, student_delete_view

urlpatterns = [
    path('', home, name="home"),
    path('list/', student_list_view, name="list_route"),
    path('add/', student_add_view, name="add_route"),
    path('detail/<int:pk>/', student_detail_view, name="detail_route"),
    path('update/<int:pk>/', student_update_view, name="update_route"),
    path('delete/<int:pk>/', student_delete_view, name="delete_route"),
]  