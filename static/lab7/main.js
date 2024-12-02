// function fillFilmList() {
//     fetch('/lab7/rest-api/films/')
//     .then (function(data) {
//         return data.json();
//     })
//     .then (function(films) {
//         let tbody = document.getElementById('film-List');
//         tbody.innerHTML = '';
//         for(let i = 0; i<films.length; i++) {
//             let tr = document.createElement('tr');

//             let tdTitle = document.createElement('td');
//             let tdTitleRus = document.createElement('td');
//             let tdYear = document.createElement('td');
//             let tdActions = document.createElement('td');

//             tdTitle.innerText = films[i].title==films[i].title_ru ? '' : films[i].title;
//             tdTitleRus.innerText = films[i].title_ru;
//             tdYear.innerText = films[i].year;

//             let editButton = document.createElement('Button');
//             editButton.innerText = 'редактировать';

//             let delButton = document.createElement('Button');
//             delButton.innerText = 'удалить';

//             tdActions.append(editButton);
//             tdActions.append(delButton);

//             tr.append(tdTitle);
//             tr.append(tdTitleRus);
//             tr.append(tdYear);
//             tr.append(tdActions);

//             tbody.append(tr);
//         }
//     })




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

function addFilm() {
    let newFilm = {
        title: prompt('Введите название фильма на английском:'),
        title_ru: prompt('Введите название фильма на русском:'),
        year: prompt('Введите год выпуска фильма:'),
        description: prompt('Введите описание фильма:')
    };

    fetch('/lab7/rest-api/films/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newFilm)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Film added with index:', data.index);
        fillFilmList();
    })
    .catch(error => console.error('Error:', error));
}

function editFilm(id) {
    let updatedFilm = {
        title: prompt('Введите новое название фильма на английском:', films[id].title),
        title_ru: prompt('Введите новое название фильма на русском:', films[id].title_ru),
        year: prompt('Введите новый год выпуска фильма:', films[id].year),
        description: prompt('Введите новое описание фильма:', films[id].description)
    };

    fetch(`/lab7/rest-api/films/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(updatedFilm)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Film updated:', data);
        fillFilmList();
    })
    .catch(error => console.error('Error:', error));
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