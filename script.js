const ip = "10.66.10.71"

fetch('http://'+ip+':5000/tasks?status=todo').then(async response => {
    const tasks = await response.json();
    const pouletElement = document.querySelector('#poulet');

    for (const task of tasks) {
        const liEl = document.createElement('li');
        liEl.textContent = task.name;
        pouletElement.append(liEl);
    }
});

fetch('http://'+ip+':5000/tasks?status=in_progress').then(async response => {
    const tasks = await response.json();
    const chickenElement = document.querySelector('#chicken');

    for (const task of tasks) {
        const liEl = document.createElement('li');
        liEl.textContent = task.name;
        chickenElement.append(liEl);
    }
});

fetch('http://'+ip+':5000/tasks?status=done').then(async response => {
    const tasks = await response.json();
    const kokidoElement = document.querySelector('#kokido');

    for (const task of tasks) {
        const liEl = document.createElement('li');
        liEl.textContent = task.name;
        kokidoElement.append(liEl);
    }
});


const addForm = document.getElementById('addForm');

addForm.onsubmit = (event) => {
    event.preventDefault();
    addValue = document.getElementById('add_input').value;
    console.log(addValue);
    link = 'http://'+ip+':5000/tasks/add?name=${addValue}';
    window.open(link, "_blank");
    fetch(link).then(location.reload());

};

