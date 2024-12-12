from django.urls import path
from . import views
from .views import add_task_view

urlpatterns=[
    path('',views.index,name='index'),
    path('tuika',views.add_task,name ='tuika'),
    path('from hiduke to task',views.get_tasks_by_date, name='from hiduke to task'),
    path('add_task/', add_task_view, name='add_task'),  # タスク追加用のURL
    
]