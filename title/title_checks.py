from clean_bug_report.title import settings_title
from clean_bug_report.cheсks.others_checks import Links


def length_title(inp):
    """Длина заголовка"""
    if len(inp) < settings_title.normal_length[0]:
        return f'Слишком короткий заголовок. Количество символов: {len(inp)}.'
    elif settings_title.normal_length[0] < len(inp) < settings_title.normal_length[1]:
        return f'Заголовок оптимальный по длине. Количество символов: {len(inp)}.'
    else:
        return f'Слишком длинный заголовок. Количество символов: {len(inp)}.'


def lots_of_suggestions(inp):
    """Сколько предложений в заголовке"""
    count = 1
    for char in inp:
        if char in settings_title.lots_of_suggestions_symbols:
            count += 1
    if count > 1:
        return f'В вашем заголовке более 1 предложения, это плохо'
    else:
        return f'В вашем заголовке 1 предложение, это хорошо'


def crazy_links(inp):
    """Ссылки в заголовке"""
    if Links.www in inp or Links.http in inp or Links.https in inp:
        return f'В вашем заголовке найдена ссылка, это плохо'
    else:
        return f'В вашем заголовке не найдены ссылки, это хорошо'


def last_of_us(inp):
    """Последний символ в заголовке"""
    if inp[-1] in settings_title.invalid_characters_at_the_end_of_the_title:
        return f'Заголовок не может заканчиваться на символ "{inp[-1]}" при текущих настройках проекта'
    else:
        return f'Кажется ваш заголовок не заканчивается на нежелательные символы, это хорошо'


def first_of_us(inp):
    """Первый символ заголовка"""
    if inp[0] == '[' and '] ' in inp and settings_title.tags == 'yes':
        return 'Ваш заголовок начинается с тега, при текущих настройках это нормально'
    elif inp[0] == '[' and '] ' in inp and settings_title.tags == 'no':
        return 'Ваш заголовок начинается с тега, при текущих настройках это недопустимо'
    else:
        return f'Ваш заголовок не начинается с тега, если он нужен укажите его в начале внутри символов []'
