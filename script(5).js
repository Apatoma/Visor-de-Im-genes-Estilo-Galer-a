document.getElementById('add-habit').addEventListener('click', () => {
    const habitText = document.getElementById('new-habit').value;
    if (habitText === '') return;

    const habitList = document.getElementById('habit-list');
    const listItem = document.createElement('li');

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.addEventListener('change', (e) => {
        listItem.style.textDecoration = e.target.checked ? 'line-through' : 'none';
    });

    listItem.textContent = habitText;
    listItem.prepend(checkbox);

    habitList.appendChild(listItem);
    document.getElementById('new-habit').value = '';
});
