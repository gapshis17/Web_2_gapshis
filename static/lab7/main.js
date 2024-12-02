let films = [];

function fillFilmList() {
    fetch('/lab7/rest-api/films/')
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        films = data; // Обновляем глобальную переменную films
        let tbody = document.getElementById('film-list');
        tbody.innerHTML = '';
        for(let i = 0; i < films.length; i++) {
            let tr = document.createElement('tr');

            let tdTitle = document.createElement('td');
            let tdTitleRus = document.createElement('td');
            let tdYear = document.createElement('td');
            let tdActions = document.createElement('td');

            tdTitle.innerText = films[i].title == films[i].title_ru ? '' : films[i].title;
            tdTitleRus.innerText = films[i].title_ru;
            tdYear.innerText = films[i].year;

            let editButton = document.createElement('button');
            editButton.innerText = 'редактировать';
            editButton.onclick = function() { editFilm(i); };

            let delButton = document.createElement('button');
            delButton.innerText = 'удалить';
            delButton.onclick = function() { deleteFilm(i); };

            tdActions.append(editButton);
            tdActions.append(delButton);

            tr.append(tdTitle);
            tr.append(tdTitleRus);
            tr.append(tdYear);
            tr.append(tdActions);

            tbody.append(tr);
        }
    });
}

function showModal() {
    document.querySelector('div.modal').style.display = 'block';
    document.getElementById('description-error').innerText = ''; // Очистка сообщения об ошибке
}

function hideModal() {
    document.querySelector('div.modal').style.display = 'none';
}

function cancel() {
    hideModal();
}

function addFilm() {
    document.getElementById('id').value = '';
    document.getElementById('title').value = '';
    document.getElementById('title-ru').value = '';
    document.getElementById('year').value = '';
    document.getElementById('description').value = '';
    showModal();
}

function sendFilm() {
    const film = {
        title: document.getElementById('title').value,
        title_ru: document.getElementById('title-ru').value,
        year: document.getElementById('year').value,
        description: document.getElementById('description').value
    };

    const url = '/lab7/rest-api/films/';
    const method = 'POST';

    fetch(url, {
        method: method,
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(film)
    })
    .then(function(resp) {
        if (resp.ok) {
            return resp.json();
        } else {
            return resp.json().then(err => { throw err; });
        }
    })
    .then(function(data) {
        fillFilmList();
        hideModal();
    })
    .catch(function(errors) {
        if (errors.description) {
            document.getElementById('description-error').innerText = errors.description;
        }
    });
}

function editFilm(id) {
    document.getElementById('id').value = id;
    document.getElementById('title').value = films[id].title;
    document.getElementById('title-ru').value = films[id].title_ru;
    document.getElementById('year').value = films[id].year;
    document.getElementById('description').value = films[id].description;
    showModal();
}

function deleteFilm(id) {
    fetch(`/lab7/rest-api/films/${id}`, {
        method: 'DELETE'
    })
    .then(response => {
        if (response.status === 204) {
            console.log('Film deleted');
            fillFilmList();
        } else {
            console.error('Error:', response.statusText);
        }
    })
    .catch(error => console.error('Error:', error));
}