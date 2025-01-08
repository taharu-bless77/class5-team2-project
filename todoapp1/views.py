import calendar
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Article
from django.utils import timezone


def add_task_view(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        task = request.POST.get('task')
        priority = request.POST.get('priority')  # 優先度を取得
        Article.objects.create(date=date, task=task, priority=priority)  # タスクを作成
        return redirect(index_view)
    return render(request, 'todoapp1/index.html', {'tasks': Article.objects.all()})

def get_tasks_by_date(request):
    date = request.GET.get('date')
    filtered_tasks = Article.objects.filter(date=date).values('task', 'priority')  # 日付に基づいてタスクをフィルタリング
    return JsonResponse(list(filtered_tasks), safe=False)

def get_tasks(request):
    tasks = Article.objects.all().values('date', 'task', 'priority')  # タスクを取得
    return JsonResponse(list(tasks), safe=False)  # JSON形式で返す

def index_view(request, year=None, month=None):
    if year is None or month is None:
        today = timezone.now()
        year = today.year
        month = today.month

    month_name = calendar.month_name[month]
    month_calendar = calendar.monthcalendar(year, month)
    tasks = Article.objects.all()  # すべてのタスクを取得

    return render(request, 'todoapp1/index.html', {
        'calendar': month_calendar,
        'month_name': month_name,
        'year': year,
        'month': month,
        'tasks': tasks
    })

def delete_task_view(request, task_id):
    if request.method == 'POST':
        try:
            task = Article.objects.get(id=task_id)
            task.delete()
            return JsonResponse({'success': True})
        except Article.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Task not found'}, status=404)
