# views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse

# 二次元リストを初期化
tasks = []

def add_task(date, task):
    tasks.append([date, task])  # 日付とタスクをリストに追加

def add_task_view(request):
    if request.method == 'POST':
        date = request.POST.get('date')  # フォームから日付を取得
        task = request.POST.get('task')  # フォームからタスクを取得
        add_task(date, task)  # タスクを追加
        return redirect('index')  # タスク追加後にインデックスページにリダイレクト
    return render(request, 'todoapp1/index.html', {'tasks': tasks})  # GETリクエストの場合はフォームを表示

def index_view(request):
    return render(request, 'todoapp1/index.html', {'tasks': tasks})  # タスクリストを表示

def get_tasks_by_date(request):
    date = request.GET.get('date')  # クエリパラメータから日付を取得
    filtered_tasks = [task for task in tasks if task[0] == date]  # 日付に基づいてタスクをフィルタリング
    return JsonResponse(filtered_tasks, safe=False)  # フィルタリングされたタスクをJSON形式で返す