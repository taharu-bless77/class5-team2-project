from django.urls import path
from . import views

urlpatterns = [    
    # タスク追加用のURL
    path('add_task/', views.add_task_view, name='add_task'),
    
    # カレンダー表示のURL
    path('', views.index_view, name='calendar'),  # 現在月のカレンダー
    path('<int:year>/<int:month>/', views.index_view, name='calendar_month'),  # 年月指定のカレンダー
]