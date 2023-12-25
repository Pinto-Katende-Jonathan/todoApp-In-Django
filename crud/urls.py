from django.urls import path
from . import views

urlpatterns = [
    path('create-todo/', views.create_todo, name='create_todo'),
    path('all-todos/', views.all_todos, name='all_todos'),
    path('edit-todo/<int:pk>', views.edit_todo, name='edit_todo'),
    path('update-todo/<int:pk>', views.update_todo, name='update_todo'),
    path('delete-todo/<int:pk>', views.delete_todo, name='delete_todo'),
]