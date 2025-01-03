document.getElementById('add-todo').addEventListener('click', function() {
    const input = document.getElementById('todo-input');
    const todoText = input.value;

    if (todoText) {
        const li = document.createElement('li');
        li.textContent = todoText;
        document.getElementById('todo-list').appendChild(li);
        input.value = ''; // 入力フィールドをクリア
    }
});

document.addEventListener('DOMContentLoaded', function() {
    // タスクを取得するエンドポイントにリクエストを送信
    fetch('/todoapp/tasks/')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(tasks => {
            const taskList = document.getElementById('task-list');
            // タスクが存在する場合
            if (tasks.length > 0) {
                tasks.forEach(task => {
                    const li = document.createElement('li');
                    li.textContent = `${task.date} - ${task.task} - 優先度: ${task.priority}`;
                    taskList.appendChild(li);
                });
            } else {
                // タスクがない場合のメッセージ
                const li = document.createElement('li');
                li.textContent = 'タスクはありません。';
                taskList.appendChild(li);
            }
        })
        .catch(error => console.error('Error fetching tasks:', error));
});