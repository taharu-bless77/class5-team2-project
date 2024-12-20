const tasks = [
    {% for task in tasks %}
        { date: new Date('{{ task.0|date:"Y-m-d" }}'), task: '{{ task.1 }}' },
    {% endfor %}
];

const date = new Date();
const today = date.getDate();
const currentMonth = date.getMonth();

function createCalendar(month) {
    const monthDays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
    const year = date.getFullYear();
    
    let calendarHTML = '<table class="calendar"><thead><tr>';
    for (let i = 0; i < 7; i++) {
        calendarHTML += `<th>${monthDays[i]}</th>`;
    }
    calendarHTML += '</tr></thead><tbody>';
    
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    const firstDay = new Date(year, month, 1).getDay();
    let dayCount = 1;
    
    for (let i = 0; i < 6; i++) {
        calendarHTML += '<tr>';
        for (let j = 0; j < 7; j++) {
            if (i === 0 && j < firstDay) {
                calendarHTML += '<td class="mute"></td>';
            } else if (dayCount > daysInMonth) {
                calendarHTML += '<td class="mute"></td>';
            } else {
                // Check for tasks on dayCount
                const taskForDay = tasks.find(task => task.date.getDate() === dayCount && task.date.getMonth() === month && task.date.getFullYear() === year);
                const taskText = taskForDay ? `<br>${taskForDay.task}` : '';

                // Highlight today
                let tdClass = (dayCount === today && month === currentMonth) ? 'today' : '';
                
                calendarHTML += `<td class="${tdClass}">${dayCount}${taskText}</td>`;
                dayCount++;
            }
        }
        calendarHTML += '</tr>';
        if (dayCount > daysInMonth) {
            break;
        }
    }
    calendarHTML += '</tbody></table>';
    return calendarHTML;
}

document.getElementById('calendar').innerHTML = createCalendar(currentMonth);