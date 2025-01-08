document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // フォームのデフォルトの送信を防ぐ

        const date = document.getElementById('date').value;
        const task = document.getElementById('task').value;
        const priority = document.getElementById('priority').value;

        // タスクを追加するためのPOSTリクエストを送信
        fetch('/todoapp/add_task/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') // CSRFトークンを取得
            },
            body: JSON.stringify({ date, task, priority })
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Network response was not ok');
        })
        .then(data => {
            // タスクをリストに追加
            const taskList = document.getElementById('task-list');
            const li = document.createElement('li');
            li.textContent = `${data.date} - ${data.task} - 優先度: ${data.priority}`;
            taskList.appendChild(li);
            // フォームをクリア
            form.reset();
        })
        .catch(error => console.error('Error adding task:', error));
    });

    // 削除ボタンのイベントリスナーを追加
    document.querySelectorAll('.delete-task').forEach(button => {
        button.addEventListener('click', function() {
            const taskId = this.getAttribute('data-id');
            fetch(`/todoapp/delete_task/${taskId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                }
            })
            .then(response => {
                if (response.ok) {
                    this.parentElement.remove(); // タスクをリストから削除
                }
            })
            .catch(error => console.error('Error deleting task:', error));
        });
    });
});

// CSRFトークンを取得する関数
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}