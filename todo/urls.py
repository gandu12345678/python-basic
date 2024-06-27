from django.urls import path

from todo.views import index

urlpatterns=[
    path("home",index)
]
