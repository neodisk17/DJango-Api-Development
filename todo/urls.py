from django.urls import path
from todo.views import TodoView

urlpatterns = [
    path("",TodoView.as_view()),
    path("<int:pk>/",TodoView.as_view()),
]
