# views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Article

def add_task_view(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        task = request.POST.get('task')
        priority = request.POST.get('priority')  # 優先度を取得
        Article.objects.create(date=date, task=task, priority=priority)  # タスクを作成
        return redirect('index')
    return render(request, 'todoapp1/index.html', {'tasks': Article.objects.all()})

def get_tasks_by_date(request):
    date = request.GET.get('date')
    filtered_tasks = Article.objects.filter(date=date).values('task', 'priority')  # 日付に基づいてタスクをフィルタリング
    return JsonResponse(list(filtered_tasks), safe=False)

def index_view(request):
    tasks = Article.objects.all()  # すべてのタスクを取得
    return render(request, 'todoapp1/index.html', {'tasks': tasks})  # タスクリストを表示
