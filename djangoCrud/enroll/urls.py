from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_show, name='addandshow'),
    path('edit/<int:id>', views.edit_show, name='updatestudent'),
    path('delete/<int:id>', views.delete_show, name='deletestudent')
]
