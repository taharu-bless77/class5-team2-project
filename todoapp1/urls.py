from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),  # インデックスページ
    path('add_task/', views.add_task_view, name='add_task'),  # タスク追加用のURL
    path('tasks/', views.get_tasks, name='get_tasks'),  # タスク取得用のURL
]