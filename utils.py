import json


def load_candidates(filename="candidates.json"):
    """Загрузит данные из файла Json"""
    with open(filename, "r", encoding='utf-8') as f:

      return json.load(f)


def get_all():
    """ Покажет всех кандидатов """
    return load_candidates()


def get_by_pk(pk):
    """ Вернет кандидата по pk """
    for candidate in load_candidates():
        if pk == candidate["pk"]:
            return candidate
    return


def get_by_skill(skill_name):
    """Вернет кандидатов по навыку"""
    candidates = []
    for candidate in load_candidates():
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            candidates.append(candidate)
    return candidates