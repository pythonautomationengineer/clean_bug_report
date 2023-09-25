from clean_bug_report.word_bases import необъективная_оценка, канцеляризмы, неинформативные_слова, оценки, маннеризм, \
    паразиты_времени, усилители, вводные, неинформативные_словосочетания, клише, неопределенность, обобщения, заумь, \
    штампы, глаголы_прошедшего_времени


class GarbageWords:
    @staticmethod
    def introductory_words(inp):
        inp_list = inp.split()
        merge_1 = set(inp_list).intersection(вводные.vvod)
        if len(merge_1) == 1:
            merge_1 = ''.join(merge_1)
            return f'{merge_1}, - вводное слово, которое лучше не использовать'
        elif len(merge_1) > 1:
            str_merge_1 = ', '.join(str(x) for x in merge_1)
            return f'Обнаружены вводные слова: {str_merge_1}. Лучше от них отказаться.'
        else:
            return 'Вводные слова не найдены, это хорошо'

    @staticmethod
    def main_cansel(inp):
        inp_list = inp.split()
        merge_2 = set(inp_list).intersection(канцеляризмы.cansel_full)
        if len(merge_2) == 1:
            merge_2 = ''.join(merge_2)
            return f'{merge_2}, - канцеляризм, который лучше не использовать'
        elif len(merge_2) > 1:
            str_merge_2 = ', '.join(str(x) for x in merge_2)
            return f'Обнаружены канцеляризмы: {str_merge_2}. Лучше от них отказаться.'
        else:
            return 'Канцеляризмы не найдены, это хорошо'

    @staticmethod
    def clishe(inp):
        inp_list = inp.split()
        merge_2 = set(inp_list).intersection(клише.klsh_full)
        if len(merge_2) == 1:
            merge_2 = ''.join(merge_2)
            return f'{merge_2}, - клише, которое лучше не использовать'
        elif len(merge_2) > 1:
            str_merge_2 = ', '.join(str(x) for x in merge_2)
            return f'Обнаружены клише: {str_merge_2}. Лучше от них отказаться.'
        else:
            return 'Клише не найдены, это хорошо'

    @staticmethod
    def shtamps(inp):
        inp_list = inp.split()
        merge_2 = set(inp_list).intersection(штампы.stmps_full)
        if len(merge_2) == 1:
            merge_2 = ''.join(merge_2)
            return f'{merge_2}, - штамп, который лучше не использовать'
        elif len(merge_2) > 1:
            str_merge_2 = ', '.join(str(x) for x in merge_2)
            return f'Обнаружены штампы: {str_merge_2}. Лучше от них отказаться.'
        else:
            return 'Штампы не найдены, это хорошо'

    @staticmethod
    def mannerizm(inp):
        inp_list = inp.split()
        merge_2 = set(inp_list).intersection(маннеризм.man_full)
        if len(merge_2) == 1:
            merge_2 = ''.join(merge_2)
            return f'{merge_2}, - маннеризм, который лучше не использовать.'
        elif len(merge_2) > 1:
            str_merge_2 = ', '.join(str(x) for x in merge_2)
            return f'Обнаружены маннеризмы: {str_merge_2}. Лучше от них отказаться.'
        else:
            return 'Маннеризмы не найдены, это хорошо'

    @staticmethod
    def neinf(inp):
        inp_list = inp.split()
        merge_2 = set(inp_list).intersection(неинформативные_слова.neinf_full)
        if len(merge_2) == 1:
            merge_2 = ''.join(merge_2)
            return f'{merge_2}, - неинформативное слово, которое лучше не использовать.'
        elif len(merge_2) > 1:
            str_merge_2 = ', '.join(str(x) for x in merge_2)
            return f'Обнаружены неинформативные слова: {str_merge_2}. Лучше от них отказаться.'
        else:
            return 'Неинформативные слова не найдены, это хорошо'

    @staticmethod
    def neob(inp):
        inp_list = inp.split()
        merge_2 = set(inp_list).intersection(необъективная_оценка.full_neob)
        if len(merge_2) == 1:
            merge_2 = ''.join(merge_2)
            return f'{merge_2}, - слово из группы "необъективная оценка". Лучше изменить его на более информативное.'
        elif len(merge_2) > 1:
            str_merge_2 = ', '.join(str(x) for x in merge_2)
            return f'Обнаружены слова из группы "необъективная оценка": {str_merge_2}. Лучше от них отказаться.'
        else:
            return 'Необъективные оценки не найдены'

    @staticmethod
    def neop(inp):
        inp_list = inp.split()
        merge_2 = set(inp_list).intersection(неопределенность.neo_full)
        if len(merge_2) == 1:
            merge_2 = ''.join(merge_2)
            return f'{merge_2}, - слово из группы "неопределенность". Лучше изменить его.'
        elif len(merge_2) > 1:
            str_merge_2 = ', '.join(str(x) for x in merge_2)
            return f'Обнаружены слова из группы "неопределенность": {str_merge_2}. Лучше от них отказаться.'
        else:
            return 'Неопределенности не найдены, это хорошо'

    @staticmethod
    def obob(inp):
        inp_list = inp.split()
        merge_2 = set(inp_list).intersection(обобщения.ob_ie_full)
        if len(merge_2) == 1:
            merge_2 = ''.join(merge_2)
            return f'{merge_2}, - слово из группы "обобщения". Лучше изменить его.'
        elif len(merge_2) > 1:
            str_merge_2 = ', '.join(str(x) for x in merge_2)
            return f'Обнаружены слова из группы "обобщения": {str_merge_2}. Лучше от них отказаться.'
        else:
            return 'Обобщения не найдены'

    @staticmethod
    def ocenki(inp):
        inp_list = inp.split()
        merge_2 = set(inp_list).intersection(оценки.ocenki_full)
        if len(merge_2) == 1:
            merge_2 = ''.join(merge_2)
            return f'{merge_2}, - слово из группы "оценки". Лучше изменить его.'
        elif len(merge_2) > 1:
            str_merge_2 = ', '.join(str(x) for x in merge_2)
            return f'Обнаружены слова из группы "оценки": {str_merge_2}. Лучше от них отказаться.'
        else:
            return 'Оценки не найдены'

    @staticmethod
    def parasites(inp):
        inp_list = inp.split()
        merge_2 = set(inp_list).intersection(паразиты_времени.parasites_full)
        if len(merge_2) == 1:
            merge_2 = ''.join(merge_2)
            return f'{merge_2}, - слово из группы "паразиты времени". Лучше изменить его.'
        elif len(merge_2) > 1:
            str_merge_2 = ', '.join(str(x) for x in merge_2)
            return f'Обнаружены слова из группы "паразиты времени": {str_merge_2}. Лучше от них отказаться.'
        else:
            return 'Паразиты времени не найдены'

    @staticmethod
    def boosters(inp):
        inp_list = inp.split()
        merge_2 = set(inp_list).intersection(усилители.boosters_full)
        if len(merge_2) == 1:
            merge_2 = ''.join(merge_2)
            return f'{merge_2}, - слово из группы "усилители". Лучше изменить его.'
        elif len(merge_2) > 1:
            str_merge_2 = ', '.join(str(x) for x in merge_2)
            return f'Обнаружены слова из группы "усилители": {str_merge_2}. Лучше от них отказаться.'
        else:
            return 'Усилители не найдены'

    @staticmethod
    def zaum(inp):
        inp_list = inp.split()
        full_set = set(inp_list).intersection(заумь.full_zaum_keys)
        list_full = list(full_set)
        list_count = len(list_full)

        if list_count > 0:
            count = f'Количество заумных слов: {list_count}.'
            f_dict = {}
            for i in list_full:
                f_dict[i] = заумь.zaum[i]
            final = ''
            for key, value in f_dict.items():
                final += f'Слово "{key}" лучше заменить на "{value}". '
            return f'{count} {final}'
        else:
            return 'Заумные слова не найдены'

    @staticmethod
    def not_information_words(inp):
        inp_list = inp.split()
        first_str = ' '.join(inp_list)
        n = 0
        b = []

        for i in неинформативные_словосочетания.full_n_s:
            if i in first_str:
                n = n + 1
                b.append(i)

        t = ', '.join(b)

        if n == 0:
            return 'Неинформативные словосочетания не найдены'
        elif n == 1:
            b = ''.join(b)
            return (f'Найдено 1 неинформативное словосочетание. Выражение "{b}" лучше заменить '
                    f'более информативными словами')
        else:
            return (f'Неинформативных словосочетаний: {n}. Словосочетания {t} лучше заменить '
                    f'более информативными словами')

    @staticmethod
    def past_tense_verbs(inp):
        inp_list = inp.split()
        full_set = set(inp_list).intersection(глаголы_прошедшего_времени.full_verbs_pv_keys)
        list_full = list(full_set)
        list_count = len(list_full)

        if list_count > 0:
            count = f'Найдено глаголов прошедшего времени: {list_count}.'
            f_dict = {}
            for i in list_full:
                f_dict[i] = глаголы_прошедшего_времени.verbs_pv[i]
            final = ''
            for key, value in f_dict.items():
                final += f'Слово "{key}" лучше заменить на "{value}". '
            return f'{count} {final}'
        else:
            return 'Глаголы прошедшего времени не найдены, это хорошо'
