import names
from clean_bug_report.cheсks.basic_checks import GarbageWords
from clean_bug_report.title.title_checks import length_title, lots_of_suggestions, crazy_links, last_of_us, first_of_us


def main():
    inp = input('Введите название поля баг-репорта, которое хотите проверить. Например "title". ').strip().lower()

    if inp in names.Names.title:
        title()
    elif inp in names.Names.preconditions:
        preconditions()
    elif inp in names.Names.actual_result:
        actual_result()
    elif inp in names.Names.expected_result:
        expected_result()


def preconditions():
    pass


def title():
    inp = input('Введите заголовок баг-репорта: ').strip().lower()
    print()

    # длина заголовка
    length_title_result = length_title(inp)
    print(length_title_result)

    # количество предложений в заголовке
    lots_of_suggestions_result = lots_of_suggestions(inp)
    print(lots_of_suggestions_result)

    # ссылка в заголовке
    crazy_links_result = crazy_links(inp)
    print(crazy_links_result)

    # последний символ заголовка
    last_of_us_result = last_of_us(inp)
    print(last_of_us_result)

    # тег в начале заголовка
    find_tag_result = first_of_us(inp)
    print(find_tag_result)

    # вводные слова
    introductory_words_result = GarbageWords.introductory_words(inp)
    print(introductory_words_result)

    # концеляризмы
    main_cansel_result = GarbageWords.main_cansel(inp)
    print(main_cansel_result)

    # клише
    clishe_result = GarbageWords.clishe(inp)
    print(clishe_result)

    # штампы
    shtamps_result = GarbageWords.shtamps(inp)
    print(shtamps_result)

    # маннеризмы
    mannerizm_result = GarbageWords.mannerizm(inp)
    print(mannerizm_result)

    # неинформативные слова
    neif_result = GarbageWords.neinf(inp)
    print(neif_result)

    # необъективная оценка
    neob_result = GarbageWords.neob(inp)
    print(neob_result)

    # неопределенности
    neop_result = GarbageWords.neop(inp)
    print(neop_result)

    # обобщения
    obob_result = GarbageWords.obob(inp)
    print(obob_result)

    # оценки
    ocenki_result = GarbageWords.ocenki(inp)
    print(ocenki_result)

    # паразиты времени
    parasites_result = GarbageWords.parasites(inp)
    print(parasites_result)

    # усилители
    boosters_result = GarbageWords.boosters(inp)
    print(boosters_result)

    # заумные слова
    zaum_result = GarbageWords.zaum(inp)
    print(zaum_result)

    # неинформативные словосочетания
    not_information_words_result = GarbageWords.not_information_words(inp)
    print(not_information_words_result)

    # глаголы прошедшего времени
    past_tense_verbs_result = GarbageWords.past_tense_verbs(inp)
    print(past_tense_verbs_result)

    print()
    main()


def actual_result():
    pass


def expected_result():
    pass


main()
