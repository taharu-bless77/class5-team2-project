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