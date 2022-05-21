# Импорт класса Flask для построения приложения
# и функции render_template для работы с шаблонами
from flask import Flask, render_template

# Импорт функций для работы с данными во вьюшках
from utils import (load_candidates_from_json,
                   get_candidate,
                   get_candidates_by_name,
                   get_candidates_by_skill)

# Конструктор приложения
app = Flask(__name__)


@app.route('/')
def page_index():
    """
    Функция представление основной страницы
    Выводит список имен кандидатов с ссылками на их профиль
    :return старница с кандидадами:
    """
    # Получаем список с данными кандидатов
    candidates = load_candidates_from_json()

    # Передаем в шаблон кандидатов
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:uid>/')
def profile_of_candidate(uid):
    """
    Функция для представления профиля кандидата по его id
    :param uid: id кандидата
    :return: профиль кандидата по id
    """
    # Получаем кандидата по id
    candidate = get_candidate(uid)

    # Передаем кандидата в шаблон для вывода его данных
    return render_template('card.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def search_by_name(candidate_name):
    """
    Функция поиска кандидатов по имени
    :param candidate_name: имя искомого кандидата
    :return: кол-во и список найденных кандидатов по имени
    """
    # Получаем список кандидатов по имени
    candidates = get_candidates_by_name(candidate_name)

    # Передаем список и кол-во кандидатов в шаблон для вывода результата поиска
    return render_template('search.html', candidates=candidates, count=len(candidates))


@app.route('/skill/<skill>')
def search_by_skill(skill):
    """
    Функция поиска кандидатов по навыку
    :param skill: навык искомый
    :return: кол-во и список найденных кандидатов по навыку
    """
    # Получаем список кандидатов по навыку
    candidates = get_candidates_by_skill(skill)

    # Передаем список и кол-во кандидатов в шаблон для вывода результата поиска
    return render_template('skill.html', candidates=candidates, count=len(candidates))


if __name__ == '__main__':
    # Запуск приложения
    app.run()

