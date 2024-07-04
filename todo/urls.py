from django.urls import path

from todo.views import index,contact,create

urlpatterns=[
    path("",index),
    path("contact",contact),
    path("create",create)
]
