from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'todoapp1/index.html')

tasks = []

def add_task(date, task):
    # タスクを追加する関数
    tasks.append([date, task])  # 日付とタスクをリストに追加

def get_tasks_by_date(date):
    # 日付に基づいてタスクを取得する関数
    return [task for task_date, task in tasks if task_date == date]

def add_task_view(request):
    if request.method == 'POST':#フォームが送信されたとき（POSTリクエスト）の処理を行います。
        date = request.POST.get('date')  # フォームから日付を取得
        task = request.POST.get('task')  # フォームからタスクを取得
        add_task(date, task)  # タスクを追加
        return redirect('index')  # タスク追加後にインデックスページにリダイレクト
    return render(request, 'todoapp1/index.html')  # GETリクエストの場合はフォームを表示

