from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('tuika',views.add_task,name ='tuika'),
    path('from hiduke to task',views.get_tasks_by_date, name='from hiduke to task'),
]