
from django.urls import path
from . import views

urlpatterns = [
    path("",views.show,name="show"),
    path("create/",views.createdata,name="create"),
    path("update/<int:id>",views.updatedata,name="update"),
    path("delete/<int:id>",views.deletedata,name="delete"),
]
