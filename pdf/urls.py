from django. urls import path
from . import views

urlpatterns = [
    path('',views.accept,name= 'accept'),
    path('<int:id>/',views.cv,name="cv"),
    path('list/',views.list,name="list"),
]