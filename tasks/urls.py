from django.urls import path
from .views import task_list, task_edit, task_delete, task_toggle

app_name = "tasks"

urlpatterns = [
    path("", task_list, name="list"),
    path("task/<int:pk>/edit/", task_edit, name="edit"),
    path("task/<int:pk>/delete/", task_delete, name="delete"),
    path("task/<int:pk>/toggle/", task_toggle, name="toggle"),
]