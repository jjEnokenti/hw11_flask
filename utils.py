from json import load

# Путь к фалу с json-данными по кандидатам
PATH_DATA = 'candidates.json'


def load_candidates_from_json(path=PATH_DATA):
    """
    Функция загрузки и конвертирования данных из json для дальнейшей работы
    :param path: путь к файлу
    :return data: форматированный список словарей с информацией по кандидатам
    """
    # Обработка файла с помощью функции load
    with open(path, 'r', encoding='utf8') as infile:
        data = load(infile)

    # Конвертированная информация
    return data


def get_candidate(candidate_id):
    """
    Функция поиска кандидата по id
    :param candidate_id: id
    :return candidate: возвращает кандидата по переданному id,
    если нет сообщает об отсутствии такого кандидата
    """
    # Вызов функции конвертации информации и сохранение ее в переменную
    data = load_candidates_from_json()

    # Цикл для поиска кандидата с нужным id среди кандидатов
    for candidate in data:
        if candidate_id == candidate['id']:
            return candidate

    # Вернется в случае отсутствия кандидата с переданным id
    return "There is no such candidate"


def get_candidates_by_name(candidate_name):
    """
    Функция поиска кандидатов по имени
    :param candidate_name: имя для поиска
    :return candidates: возвращает список кандидатов по имени либо пустой список
    """
    # Вызов функции конвертации информации и сохранение ее в переменную
    data = load_candidates_from_json()

    # Приведение имени в нижний регистр для исключения ошибок
    candidate_name = candidate_name.lower()
    # Создание пустого списка, для дальнейшего складывания в него кандидатов
    candidates = []

    # Цикл по поиску кандидатов
    for candidate in data:
        # Если имя входит в имя кандидата, то кладем кандидата в список
        if candidate_name in candidate['name'].lower():
            candidates.append(candidate)

    # возвращает список кандидатов
    return candidates


def get_candidates_by_skill(skill):
    """
    Функция поиска кандидатов по навыку
    :param skill: навык по каторуму ищим кандидатов
    :return candidates: список кандидатов по навыку
    """
    # Вызов функции конвертации информации и сохранение ее в переменную
    data = load_candidates_from_json()

    # Приведение навыка в нижний регистр для исключения ошибок
    skill = skill.lower()
    # Создание пустого списка, для дальнейшего складывания в него кандидатов
    candidates = []

    # Цикл по поиску кандидатов
    for candidate in data:
        # Если навык есть у кандидата, то кладем кандидата в список
        if skill in candidate['skills'].lower().split(', '):
            candidates.append(candidate)

    # возвращает список кандидатов
    return candidates

