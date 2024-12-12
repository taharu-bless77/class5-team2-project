from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),  # インデックスページ
    path('add_task/', views.add_task_view, name='add_task'),  # タスク追加用のURL
    path('tasks_by_date/', views.get_tasks_by_date, name='tasks_by_date'),  # 日付に基づくタスク取得
]