import random
import local as lcl


def student_1(th, tsks, lk, tchr, cnd, a, b, c, d, e):
    theory = th + a
    tasks = tsks + b
    luck = lk + c
    teacher = tchr + d
    condition = cnd + e
    print("theory=", theory,
          "tasks=", tasks,
          "luck=", luck,
          "teacher=", teacher,
          "condition=", condition)
    return student_1


def student_2(th, tsks, lk, tchr, cnd, a, b, c, d, e):
    theory = th + a
    tasks = tsks + b
    luck = lk + c
    teacher = tchr + d
    condition = cnd + e
    print("theory=", theory,
          "tasks=", tasks,
          "luck=", luck,
          "teacher=", teacher,
          "condition=", condition)
    return student_2


def student_3(th, tsks, lk, tchr, cnd, a, b, c, d, e):
    theory = th + a
    tasks = tsks + b
    luck = lk + c
    teacher = tchr + d
    condition = cnd + e
    print("theory=", theory,
          "tasks=", tasks,
          "luck=", luck,
          "teacher=", teacher,
          "condition=", condition)
    return student_3


def day_1():
    print(f"{lcl.INTRODUCTION_DAY_1}")
    print(f"{lcl.MANIUAL_DAY_1}")
    cases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = random.choice(cases)
    match m:
        case 1:
            e = 90
            a, b, c, d = (0,) * 4
            print("Ты проснулся, а сегодня замечательная погода, "
                  "+ вайб(состояние)")
        case 2:
            e = -90
            a, b, c, d = (0,) * 4
            print("Сегодня тебе приснился кошмар, теперь ты боишься бабайку."
                  "Весь день на стрессе(состояние ухудшилось)")
        case 3:
            c = 100
            a, b, e, d = (0,) * 4
            print("Сегодня ты увидел падающую звезду и "
                  "загадал желание - плюс удача")
        case 4:
            print("Ты нравишься старшекурснику/старшекурснице."
                  " тебе скинули расписанные билеты с полезными пометками "
                  "(йоу, да ты красотка/мачо""+ теория")
            a = 80
            e, b, c, d = (0,) * 4
        case 5:
            c = -80
            d = -60
            a, b, e = (0,) * 3
            print("Ты рассыпал соль — к ссорам и неудачам. "
                  "Твои отношения с преподавателем и удача снизились в течение следующих 8 лет")
        case 6:
            b = 80
            a, e, c, d = (0,) * 4
            print("Ты попал на бал великих математиков, они тебе все объяснили"
                  " доступным языком(тралалело тралала)")
        case 7:
            b = -70
            a, e, c, d = (0,) * 4
            print("Под окном орут студенты "
                  "и тебе трудно сконцентрироваться (УК РФ ст.105…..)"
                  "-задачи")
        case 8:
            a = -80
            e, b, c, d = (0,) * 4
            print("Тебя отвлекает шум машин за окном "
                  "(за намеренный прокол колеса штраф дают, "
                  "одумайся. УК РФ ст.167)""-теория(")
        case 9:
            d = 90
            a, b, c, e = (0,) * 4
            print("Ты улыбался другу, а преподаватель подумал,"
                  " что ему, он поздоровался с тобой"
                  " и улыбнулся в ответ""+ к отношению с преподавателем")
        case 10:
            d = -90
            a, b, c, e = (0,) * 4
            print("На твоём телефоне произошел глюк и он отправил сообщение"
                  " в 3 часа ночи не в ту группу,"
                  " а в группу с преподавателем из за чего он проснулся "
                  "- отношения с преподавателем")

    k = int(input(""))
    match k:
        case 1:
            student_1(500, 500, 500, 500, 500, a, b, c, d, e)
            th = 500 + a
            tsks = 500 + b
            lk = 500 + c
            tchr = 500 + d
            cnd = 500 + e
        case 2:
            student_2(500, 500, 500, 500, 500, a, b, c, d, e)
            th = 500 + a
            tsks = 500 + b
            lk = 500 + c
            tchr = 500 + d
            cnd = 500 + e
        case 3:
            student_3(500, 500, 500, 500, 500, a, b, c, d, e)
            th = 500 + a
            tsks = 500 + b
            lk = 500 + c
            tchr = 500 + d
            cnd = 500 + e
    cases_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = random.choice(cases_1)
    match m:
        case 1:
            e = 80
            a, b, c, d = (0,) * 4
            print("Любимый артист выпустил крутую песню, которая тебя подбодрила"
                  "и замотивировала(+ к состоянию)")
        case 2:
            e = -50
            a, b, c, d = (0,) * 4
            print("На тебя чихнул сосед, ты заболел (больше не здоровайся с ним..)")
        case 3:
            c = 100
            e = 80
            a, b, d = (0,) * 3
            print("Неожиданно, ты вспоминаешь о видео поздравлении на 8 марта/23 февраля"
                  " и понимаешь,что удача сегодня на твоей стороне"
                  " - плюс баллы удачи и состояния")
        case 4:
            print("Ты знаешь всю эту теорию со школы (ты оксфорд или хогвартс закончил?)")
            a = 80
            e, b, c, d = (0,) * 4
        case 5:
            c = -80
            a, b, d, e = (0,) * 4
            print("Проснувшись, ты разбил зеркало теперь тебя ждет семь лет неудач.")
        case 6:
            b = 80
            a, e, c, d = (0,) * 4
            print("Ты научился управлять временем и у тебя куча времени на то,"
                  " чтобы освоить навыки решения задач по матану")
        case 7:
            b = - 70
            a, e, c, d = (0,) * 4
            print("Под окном орут студенты "
                  "и тебе трудно сконцентрироваться (УК РФ ст.105…..)"
                  "-задачи")
        case 8:
            a = -80
            e, b, c, d = (0,) * 4
            print("Ты спал головой на север и знания сдулись"
                  "(хахахах,ну минус теория получается)")
        case 9:
            d = 90
            a, b, c, e = (0,) * 4
            print("Ты улыбался другу, а преподаватель подумал,"
                  " что ему, он поздоровался с тобой"
                  " и улыбнулся в ответ""+ к отношению с преподвавателем")
        case 10:
            d = -90
            a, b, c, e = (0,) * 4
            print("На твоём телефоне произошел глюк и он отправил сообщение"
                  " в 3 часа ночи не в ту группу,"
                  " а в группу с преподавателем из за чего он проснулся "
                  "- отношения с преподавателем")
    k = int(input(""))
    match k:
        case 1:
            student_1(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 2:
            student_2(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 3:
            student_3(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
    cases_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = random.choice(cases_2)
    match m:
        case 1:
            e = 80
            a, b, c, d = (0,) * 4
            print("Твои друзья отправили тебе посылку со сладостями,"
                  " чтобы подбодрить во время подготовки(милота, + состояние)")
        case 2:
            e = -80
            a, b, c, d = (0,) * 4
            print("Любимые соседи решили устроить ремонт, из-за шума у тебя болит голова"
                  "и ты не можешь нормально выспаться(-состояние)")
        case 3:
            c = 100
            a, b, e, d = (0,) * 4
            print("Сегодня ты увидел падающую звезду и "
                  "загадал желание - плюс удача")
        case 4:
            print("Ты нравишься старшекурснику/старшекурснице."
                  " тебе скинули расписанные билеты с полезными пометками "
                  "(йоу, да ты красотка/мачо""+ теория")
            a = 80
            e, b, c, d = (0,) * 4
        case 5:
            c = -100
            a, b, d, e = (0,) * 4
            print("Во сне ты увидел женщину с пустыми вёдрами — к неудаче.")
        case 6:
            b = 80
            a, e, c, d = (0,) * 4
            print("Ты попал на бал великих математиков, они тебе все объяснили"
                  " доступным языком(тралалело тралала)")
        case 7:
            b = -80
            a, e, c, d = (0,) * 4
            print("Под окном орут студенты "
                  "и тебе трудно сконцентрироваться (УК РФ ст.105…..)"
                  "-задачи")
        case 8:
            a = -80
            e, b, c, d = (0,) * 4
            print("Тебя отвлекает шум машин за окном "
                  "(за намеренный прокол колеса штраф дают, "
                  "одумайся. УК РФ ст.167)""-теория(")
        case 9:
            d = 90
            a, b, c, e = (0,) * 4
            print(" Сегодня ты поднял чью то куртку, потому что она упала с крючка в коридоре,"
                  " а это оказалась куртка преподавателя( он видел, что ты её поднял, плюс уважение!) ")
        case 10:
            d = -90
            a, b, c, e = (0,) * 4
            print("Тебя случайно толкнули и ты врезался в преподавателя(минус в карму)")
    k = int(input(""))
    match k:
        case 1:
            student_1(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 2:
            student_2(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 3:
            student_3(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
    cases_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = random.choice(cases_3)
    match m:
        case 1:
            e = 70
            a, b, c, d = (0,) * 4
            print("Ты проснулся, а сегодня замечательная погода, "
                  "+ вайб(состояние)")
        case 2:
            e = -70
            a, b, c, d = (0,) * 4
            print("Сегодня тебе приснился кошмар,теперь ты боишься бабайку"
                  "Весь день на стрессе(состояние ухудшилось)")
        case 3:
            c = 100
            a, b, e, d = (0,) * 4
            print("Сегодня ты увидел падающую звезду и "
                  "загадал желание - плюс удача")
        case 4:
            print("Ты нравишься старшекурснику/старшекурснице."
                  " тебе скинули расписанные билеты с полезными пометками "
                  "(йоу, да ты красотка/мачо""+ теория")
            a = 80
            e, b, c, d = (0,) * 4
        case 5:
            c = -80
            d = -70
            a, b, e = (0,) * 3
            print("Рассыпать соль — к ссорам и неудачам. "
                  "Твои отношения с преподавателем и удача снизились")
        case 6:
            b = 80
            a, e, c, d = (0,) * 4
            print("Ты попал на бал великих математиков, они тебе все объяснили"
                  " доступным языком(тралалело тралала)")
        case 7:
            b = - 70
            a, e, c, d = (0,) * 4
            print("Под окном орут студенты "
                  "и тебе трудно сконцентрироваться (УК РФ ст.105…..)"
                  "-задачи")
        case 8:
            a = -80
            e, b, c, d = (0,) * 4
            print("Тебя отвлекает шум машин за окном "
                  "(за намеренный прокол колеса штраф дают, "
                  "одумайся. УК РФ ст.167)""-теория(")
        case 9:
            d = 70
            a, b, c, e = (0,) * 4
            print("Ты улыбался другу, а преподаватель подумал,"
                  " что ему, он поздоровался с тобой"
                  " и улыбнулся в ответ""+ к отношению с преподавателем")
        case 10:
            d = -90
            a, b, c, e = (0,) * 4
            print("На твоём телефоне произошел глюк и он отправил сообщение"
                  " в 3 часа ночи не в ту группу,"
                  " а в группу с преподавателем из за чего он проснулся "
                  "- отношения с преподавателем")
    k = int(input(""))
    match k:
        case 1:
            student_1(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 2:
            student_2(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 3:
            student_3(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e

    cases_4 = [1, 2, 3, 4, 5]
    m = random.choice(cases_4)
    match m:
        case 1:
            print("Пришло время делать выбор. Пойдёшь прогуляться на уличице или нет?"
                  "Помни, что на улице тебе может полегчать, но также мир полон опасностей"
                  " (Введи 1, если да и 2, если нет)")
            awns = int(input())
            match awns:
                case 1:
                    e = -80
                    b = -70
                    a, c, d = (0,) * 3
                    print("Эх ты, добрая душа, вышел на улицу и погладил кота."
                          "Теперь ты что то одхватил и у тебя поднялась темература из за неё ухудшилось состояние "
                          "и теперь задачки ты не сможешь порешать, а в голове долго всё не держится")
                case 2:
                    b = 70
                    a, c, d, e = (0,) * 4
                    print("Ну ты и домосед. Но зато с тобой ничего не случилось и ты немного порешал задачки"
                          " + к задачкам")
        case 2:
            print("Уделять больше времени на подготовку к теории или практике?"
                  "Перед тобой важный выбор чему уделить больше внимания,"
                  " однако придётся чем то жертвовать."
                  " (Введи 1, если выберешь теорию, 2, если практику и 3, если всего понемногу)")
            awns = int(input())
            match awns:
                case 1:
                    a = 100
                    b = -80
                    e, c, d = (0,) * 3
                    print("Ты сделал свой выбор, теория на высоте, но практика пострадала")
                case 2:
                    b = 100
                    a = -80
                    c, d, e = (0,) * 3
                    print("Ты сделал свой выбор, практика на высоте, но теория пострадала пострадала")
                case 3:
                    b = 70
                    a = 70
                    c, d, e = (0,) * 3
                    print("Баланс- хорошая тактика. Мог бы получить в 2 раза больше,"
                          " но зато ничего не потерял")
        case 3:
            print("Использовать метод Помодоро?(Не гугли что это, доверься своим ощущениям)"
                  " (Введи 1, если да и 2, если нет)")
            awns = int(input())
            match awns:
                case 1:
                    a = 90
                    b, e, c, d = (0,) * 4
                    print("Ты правильно организовал свое время и не перетруждался +теория")
                case 2:
                    a = -100
                    c, d, e, b = (0,) * 4
                    print("Ну ты лузер, очевидно же, что нужно было выбирать да")
        case 4:
            print("Написать своему школьному учителю по математике?"
                  "(Введи 1, если да и 2, если нет)")
            awns = int(input())
            match awns:
                case 1:
                    a = 100
                    e = -120
                    b, c, d = (0,) * 3
                    print("Тебе объяснили теорию и она стаа намного лучше, "
                          "но на тебя напала очень сильная ностальгия у твоё состояние сильно упало")
                case 2:
                    a, c, d, e, b = (0,) * 5
                    print("Ничего страшного, что не написал, твои показатели остались прежними")
        case 5:
            print(" У тебя есть возможность позадавать преподавателю глупые вопросы,"
                  " похвалить его прикид, его парфюм( тогда прибавиться показатель осп),"
                  " однако твои братаны будут называть тебя подлизой и твоё состояние ухудшится(да/нет)."
                  " Взвесь всё, что из этого понесёт большие потери?"
                  "(Введи 1, если да и 2, если нет)")
            awns = int(input())
            match awns:
                case 1:
                    d = 100
                    e = -90
                    b, c, a = (0,) * 3
                    print("Не переживай, твои братки всё понимают, это игра на выживание")
                case 2:
                    d = -50
                    a, c, e, b = (0,) * 4
                    print("Ты не сильно примечательная личность, "
                          "поэтому преподаватель стал забывать тебя, можно было и предпринять что нибудь")
    k = int(input())
    match k:
        case 1:
            student_1(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 2:
            student_2(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 3:
            student_3(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
    print("Вот и подошёл к концу первый день подготовки, не переживай, шансы на победу есть"
          "вот, кстати твои показатели, с которыми ты закончил день. "
          "Они тебе пригодятся для второго дня, а пока ход переходит к твоему другу"
          "(для перехода ко второй команде нажмите enter)")
    print(th, tsks, lk, tchr, cnd)


def day_2():
    print(f"{lcl.INTRODUCTION_DAY_2} ")
    print(f"{lcl.MANIUAL_DAY_2}")
    th, tsks, lk, tchr, cnd = map(int, input().split())
    cases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = random.choice(cases)
    match m:
        case 1:
            e = 50
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_7}")
        case 2:
            e = -50
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_8}")
        case 3:
            c = 100
            a, b, e, d = (0,) * 4
            print(f"{lcl.LUCK_R_7}")
        case 4:
            print(f"{lcl.THEORY_R_5}")
            a = 80
            e, b, c, d = (0,) * 4
        case 5:
            d = -60
            a, b, e, c = (0,) * 4
            print(f"{lcl.LECTURER_R_6}")
        case 6:
            b = 80
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_4}")
        case 7:
            b = -70
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_5}")
        case 8:
            a = -80
            e, b, c, d = (0,) * 4
            print(f"{lcl.THEORY_R_6}")
        case 9:
            d = 50
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_7}")
        case 10:
            c = -60
            d = -90
            a, b, e = (0,) * 3
            print(f"{lcl.LUCK_R_6}")

    k = int(input(""))
    match k:
        case 1:
            student_1(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 2:
            student_2(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 3:
            student_3(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
    cases_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = random.choice(cases_1)
    match m:
        case 1:
            e = 50
            a, b, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_6}")
        case 2:
            e = -50
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_8}")
        case 3:
            c = 100
            a, b, e, d = (0,) * 4
            print(f"{lcl.LUCK_R_7}")
        case 4:
            print(f"{lcl.THEORY_R_7}")
            a = 80
            e, b, c, d = (0,) * 4
        case 5:
            d = -60
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_8}")
        case 6:
            b = 80
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_4}")

        case 7:
            b = -70
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_5}")
        case 8:
            a = -80
            e, b, c, d = (0,) * 4
            print(f"{lcl.THEORY_R_6}")
        case 9:
            d = 50
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_7}")
        case 10:
            c = -100
            d = -90
            a, b, e = (0,) * 3
            print(f"{lcl.LUCK_R_6}")
    k = int(input(""))
    match k:
        case 1:
            student_1(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 2:
            student_2(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 3:
            student_3(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
    cases_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = random.choice(cases_2)
    match m:
        case 1:
            e = 50
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_9}")
        case 2:
            e = -50
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_10}")
        case 3:
            c = 100
            a, b, e, d = (0,) * 4
            print(f"{lcl.LUCK_R_7}")
        case 4:
            print(f"{lcl.THEORY_R_7}")
            a = 80
            e, b, c, d = (0,) * 4
        case 5:
            d = -60
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_8}")
        case 6:
            b = 80
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_4}")

        case 7:
            b = -70
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_5}")
        case 8:
            a = -80
            e, b, c, d = (0,) * 4
            print(f"{lcl.THEORY_R_6}")
        case 9:
            d = 50
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_7}")
        case 10:
            c = -100
            d = -90
            a, b, e = (0,) * 3
            print(f"{lcl.LUCK_R_6}")

    k = int(input(""))
    match k:
        case 1:
            student_1(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 2:
            student_2(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 3:
            student_3(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
    cases_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = random.choice(cases_3)
    match m:
        case 1:
            e = 50
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_7}")
        case 2:
            e = -50
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_8}")
        case 3:
            c = 100
            a, b, e, d = (0,) * 4
            print(f"{lcl.LUCK_R_7}")
        case 4:
            print(f"{lcl.THEORY_R_7}")
            a = 80
            e, b, c, d = (0,) * 4
        case 5:
            d = -60
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_8}")
        case 6:
            b = 80
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_4}")
        case 7:
            b = -70
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_5}")
        case 8:
            a = -80
            e, b, c, d = (0,) * 4
            print(f"{lcl.THEORY_R_6}")
        case 9:
            d = 50
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_7}")
        case 10:
            c = -100
            d = -90
            a, b, e = (0,) * 3
            print(f"{lcl.LUCK_R_6}")

    cases_4 = [1, 2, 3, 4, 5]
    m = random.choice(cases_4)
    match m:
        case 1:
            print(f"{lcl.DEPENDENT_6}")
            awns = int(input())
            match awns:
                case 1:
                    e = 100
                    a, c, d, b = (0,) * 4
                    print(f"{lcl.RESULT_D6_1}")
                case 2:
                    e = -100
                    a, c, d, b = (0,) * 4
                    print(f"{lcl.RESULT_D6_2}")
        case 2:
            print(f"{lcl.DEPENDENT_7}")
            awns = int(input())
            match awns:
                case 1:
                    e = 100
                    b = -80
                    a, c, d = (0,) * 3
                    print(f"{lcl.RESULT_D7_1}")
                case 2:
                    print(f"{lcl.DEPENDENT_8}")
                    awns_1 = int(input())
                    match awns_1:
                        case 1:
                            e = 80
                            a = 50
                            c, d, b = (0,) * 3
                            print(f"{lcl.RESULT_D8_1}")
                        case 2:
                            print(f"{lcl.DEPENDENT_9}")
                            awns_2 = int(input())
                            match awns_2:
                                case 1:
                                    e = 30
                                    a = 30
                                    c, d, b = (0,) * 3
                                    print(f"{lcl.RESULT_D9_1}")
                                case 2:
                                    e = -80
                                    a = 10
                                    c, d, b = (0,) * 3
                                    print(f"{lcl.RESULT_D9_2}")
                case 3:
                    b = 40
                    a = 40
                    c, d, e = (0,) * 3
                    print(f"{lcl.RESULT_D8_2}")
        case 3:
            print(f"{lcl.DEPENDENT_10}")
            awns = int(input())
            match awns:
                case 1:
                    c = 180
                    b, e, a, d = (0,) * 4
                    print(f"{lcl.RESULT_D10_1}")
                case 2:
                    c, d, e, b, a = (0,) * 5
                    print(f"{lcl.RESULT_D10_2}")
        case 4:
            print(f"{lcl.DEPENDENT_11}")
            awns = int(input())
            match awns:
                case 1:
                    (th_1, tsks_1, lk_1,
                     tchr_1, cnd_1) = map(int, input(f"{lcl.RULES_FOR_2_DAY}").split())
                    th_2 = th_1
                    tsks_2 = tsks_1
                    lk_2 = lk_1 - 100
                    tchr_2 = tchr_1
                    cnd_2 = cnd_1 + 50
                    print(th_2, tsks_2, lk_2, tchr_2, cnd_2)
                    e = 100
                    b, c, d, a = (0,) * 4
                    print(f"{lcl.RESULT_D11_1}")
                case 2:
                    a, c, d, e, b = (0,) * 5
                    print(f"{lcl.RESULT_D11_2}")
        case 5:
            print(f"{lcl.DEPENDENT_12}")
            awns = int(input())
            match awns:
                case 1:
                    (th_1, tsks_1, lk_1,
                     tchr_1, cnd_1) = map(int, input(f"{lcl.RULES_FOR_2_DAY_2}").split())
                    th_2 = th_1
                    tsks_2 = tsks_1
                    lk_2 = lk_1 - 150
                    tchr_2 = tchr_1
                    cnd_2 = cnd_1
                    print(th_2, tsks_2, lk_2, tchr_2, cnd_2)
                    e = 30
                    b, c, d, a = (0,) * 4
                    print(f"{lcl.RESULT_D12_1}")
        case 2:
            e = -100
            c, d, a, b = (0,) * 4
            print(f"{lcl.RESULT_D12_2}")
    k = int(input(""))
    match k:
        case 1:
            student_1(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 2:
            student_2(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 3:
            student_3(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
    cases_5 = [1, 2, 3, 4, 5]
    m = random.choice(cases_5)
    match m:
        case 1:
            print(f"{lcl.DEPENDENT_13}")
            awns = int(input())
            match awns:
                case 1:
                    b = -100
                    c = 150
                    a, e, d = (0,) * 3
                    print(f"{lcl.RESULT_D13_1}")
                case 2:
                    a, c, d, b, e = (0,) * 5
                    print(f"{lcl.RESULT_D13_2}")
        case 2:
            print(f"{lcl.DEPENDENT_14}")
            awns = int(input())
            match awns:
                case 1:
                    n = [1, 2]
                    n_1 = random.choice(n)
                    match n_1:
                        case 1:
                            d = -100
                            a, c, b, e = (0,) * 4
                            print(f"{lcl.RESULT_D14_1}")
                        case 2:
                            d = 100
                            a, c, b, e = (0,) * 4
                            print(f"{lcl.RESULT_D14_3}")
                case 2:
                    a, c, b, e, d = (0,) * 5
                    print(f"{lcl.RESULT_D14_2}")

        case 3:
            print(f"{lcl.DEPENDENT_15}")
            awns = int(input())
            match awns:
                case 1:
                    a = 100
                    b, e, c, d = (0,) * 4
                    print(f"{lcl.RESULT_D15_1}")
                case 2:
                    a = -100
                    c, d, e, b = (0,) * 4
                    print(f"{lcl.RESULT_D15_2}")
        case 4:
            print(f"{lcl.DEPENDENT_16}")
            awns = int(input())
            match awns:
                case 1:
                    (th_1, tsks_1, lk_1,
                     tchr_1, cnd_1) = map(int, input(f"{lcl.RULES_FOR_2_DAY_3}").split())
                    th_2 = th_1 + 100
                    tsks_2 = tsks_1
                    lk_2 = lk_1
                    tchr_2 = tchr_1
                    cnd_2 = cnd_1 + 50
                    print(th_2, tsks_2, lk_2, tchr_2, cnd_2)
                    a = 80
                    e = 80
                    b, c, d = (0,) * 3
                    print(f"{lcl.RESULT_D16_1}")
                case 2:
                    (th_1, tsks_1, lk_1,
                     tchr_1, cnd_1) = map(int, input(f"{lcl.RULES_FOR_2_DAY_3}").split())
                    th_2 = th_1 - 80
                    tsks_2 = tsks_1
                    lk_2 = lk_1
                    tchr_2 = tchr_1
                    cnd_2 = cnd_1
                    print(th_2, tsks_2, lk_2, tchr_2, cnd_2)
                    e = -100
                    b, c, d, a = (0,) * 4
                    print(f"{lcl.RESULT_D16_2}")
        case 5:
            print(f"{lcl.DEPENDENT_17}")
            awns = int(input())
            match awns:
                case 1:
                    b = 80
                    a, c, d, e = (0,) * 4
                    print(f"{lcl.RESULT_D17_1}")
                case 2:
                    e = -80
                    c, d, a, b = (0,) * 4
                    print(f"{lcl.RESULT_D17_2}")
    k = int(input(""))
    match k:
        case 1:
            student_1(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 2:
            student_2(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 3:
            student_3(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
    print(f"{lcl.CONCLUSION_DAY_2}")
    print(th, tsks, lk, tchr, cnd)

