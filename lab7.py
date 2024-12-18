from flask import Blueprint, jsonify, render_template, request,url_for

lab7 = Blueprint('lab7', __name__)

films = [
    {
        "title": "There Will Be Blood",
        "title_ru": "Нефть",
        "year": 2007,
        "description": "Начало XX века. Предприниматель Дэниэл Плэйнвью ищет золото и серебро, а находит нефть.\
        За несколько лет он становится преуспевающим нефтяником, разработавшим уже несколько скважин. Однажды\
        он узнает про новое месторождение. Уцепившись за этот шанс разбогатеть, Дэниэл делает всё, чтобы добиться своего."
    },
    {
        "title": "Mulholland Dr.",
        "title_ru": "Малхолланд Драйв",
        "year": 2001,
        "description": "Загадочная девушка, после автомобильной аварии страдающая потерей памяти, выбирает себе имя Рита\
        с рекламного плаката к фильму с Ритой Хейворт и пытается начать новую жизнь в Голливуде.\
        Но тайны прошлого неотступно преследуют ее.\
        Кто были те двое мужчин, что сидели в одной машине с ней и погибли в аварии? Почему полиция подозревает, что она\
        была ими похищена? И случайно ли в ее жизни появляется новая подруга, начинающая актриса Бетти?"
    },
    {
        "title": "Sen to Chihiro no kamikakushi",
        "title_ru": "Унесённые призраками",
        "year": 2001,
        "description": "Тихиро с мамой и папой переезжает в новый дом. Заблудившись по дороге, они оказываются в\
        странном пустынном городе, где их ждет великолепный пир. Родители с жадностью набрасываются на еду и к ужасу\
        девочки превращаются в свиней, став пленниками злой колдуньи Юбабы. Теперь, оказавшись одна среди волшебных\
        существ и загадочных видений, Тихиро должна придумать, как избавить своих родителей от чар коварной старухи."
    },
    {
        "title": "Dogville",
        "title_ru": "Догвилль",
        "year": 2003,
        "description": "Юная Грейс, сбежав от банды гангстеров, находит спасение в маленьком городке Догвилль где-то\
        в Скалистых горах. Местные жители – один прекраснее другого – готовы ее укрыть. А взамен им совсем ничего не\
        надо, ну, разве что помочь по дому или присмотреть за детьми. Но постепенно милый Догвилль превращается\
        для девушки в тюрьму."
    },
    {
        "title": "No Country for Old Men",
        "title_ru": "Старикам тут не место",
        "year": 2007,
        "description": "Обычный работяга обнаруживает в пустыне гору трупов, набитый героином грузовик и\
        соблазнительную сумму в два миллиона долларов наличными. Он решает взять деньги себе, и результатом\
        становится волна насилия, которую не может остановить вся полиция Западного Техаса."
    }
]

@lab7.route('/')
def main():
    return render_template('lab7/index.html')


@lab7.route('/rest-api/films/', methods=['GET'])
def get_films():
    return jsonify(films)

@lab7.route('/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    if 0 <= id < len(films):
        return jsonify(films[id])
    else:
        return jsonify({"error": "Film not found"}), 404

@lab7.route('/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    if 0 <= id < len(films):
        films.pop(id)
        return '', 204
    else:
        return jsonify({"error": "Film not found"}), 404

@lab7.route('/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    film = request.get_json()
    if not film.get('description'):
        return jsonify({"description": "Заполните описание"}), 400
    films[id] = film
    return jsonify(films[id])

@lab7.route('/rest-api/films/', methods=['POST'])
def post_film():
    film = request.get_json()
    if not film.get('description'):
        return jsonify({"description": "Заполните описание"}), 400
    films.append(film)
    return jsonify({"index": len(films) - 1})
    