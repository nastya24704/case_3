import random
import local as lcl

def student_1(th,tsks,lk,tchr,cnd,a,b,c,d,e):
    theory=th+a
    tasks=tsks+b
    luck=lk+c
    teacher=tchr+d
    condition=cnd+e
    print("theory=", theory,
     "tasks=", tasks,
     "luck=", luck,
     "teacher=", teacher,
     "condition=", condition)
    return student_1

def student_2(th,tsks,lk,tchr,cnd,a,b,c,d,e):
    theory=th+a
    tasks=tsks+b
    luck=lk+c
    teacher=tchr+d
    condition=cnd+e
    print("theory=", theory,
     "tasks=", tasks,
     "luck=", luck,
     "teacher=", teacher,
     "condition=", condition)
    return student_2
def student_3(th,tsks,lk,tchr,cnd,a,b,c,d,e):
    theory=th+a
    tasks=tsks+b
    luck=lk+c
    teacher=tchr+d
    condition=cnd+e
    print("theory=", theory,
     "tasks=", tasks,
     "luck=", luck,
     "teacher=", teacher,
     "condition=", condition)
    return student_3

def day_1():
  print(f"{lcl.INTRODUCTION_DAY_1} ")
  print(f"{lcl.MANIUAL_DAY_1}")
  cases=[1,2,3,4,5,6,7,8,9,10]
  m = random.choice(cases)
  match m:
    case 1:
     e=50
     a,b,c,d=(0,)*4
     print("Ты проснулся, а сегодня замечательная погода, "
           "+ вайб(состояние)")
    case 2:
     e = -50
     a, b, c, d = (0,) * 4
     print("Сегодня тебе приснился кошмар, теперь ты боишься бабайку"
           "Весь день на стрессе(состояние ухудшилось)")
    case 3:
     c = 100
     a, b, e, d = (0,) * 4
     print("Сегодня тыувидел падающую звезду и "
           "загадал желание - плюс удача")
    case 4:
     print("Ты нравишься старшекурснику/старшекурснице."
           " тебе скинули расписанные билеты с полезными пометками "
           "(йоу, да ты красотка/мачо""+ теория")
     a = 80
     e, b, c, d = (0,) * 4
    case 5:
     c = -80
     d= -60
     a, b, e = (0,) * 3
     print("Рассыпать соль — к ссорам и неудачам. "
          "Твои отношения с преподавателем и удача снизились")
    case 6:
     b = 80
     a, e, c, d = (0,) * 4
     print("Ты попал на бал великих математиков, они тебе все объяснили"
          " доступным языком(тралалело тралала)")
    case 7:
     b =- 70
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
     d = 50
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

  k=int(input(""))
  match k:
    case 1:
     student_1(500,500,500,500,500,a,b,c,d,e)
     th=500+a
     tsks=500+b
     lk=500+c
     tchr=500+d
     cnd=500+e
    case 2:
     student_2(500,500,500,500,500,a,b,c,d,e)
     th=500+a
     tsks=500+b
     lk=500+c
     tchr=500+d
     cnd=500+e
    case 3:
     student_3(500,500,500,500,500,a,b,c,d,e)
     th=500+a
     tsks=500+b
     lk=500+c
     tchr=500+d
     cnd=500+e
  cases_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  m = random.choice(cases_1)
  match m:
      case 1:
          e = 50
          a, b, c, d = (0,) * 4
          print("Ты проснулся, а сегодня замечательная погода, "
                "+ вайб(состояние)")
      case 2:
          e = -50
          a, b, c, d = (0,) * 4
          print("Сегодня тебе приснился кошмар,теперь ты боишься бабайку"
                "Весь день на стрессе(состояние ухудшилось)")
      case 3:
          c = 100
          a, b, e, d = (0,) * 4
          print("Сегодня тыувидел падающую звезду и "
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
          d = 50
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
  k=int(input(""))
  match k:
    case 1:
     student_1(th,tsks,lk,tchr,cnd,a,b,c,d,e)
     th=th+a
     tsks=tsks+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
    case 2:
     student_2(th,tsks,lk,tchr,cnd,a,b,c,d,e)
     th=th+a
     tsks=tsks+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
    case 3:
     student_3(th,tsks,lk,tchr,cnd,a,b,c,d,e)
     th=th+a
     tsks=tsks+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
  cases_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  m = random.choice(cases_2)
  match m:
      case 1:
          e = 50
          a, b, c, d = (0,) * 4
          print("Ты проснулся, а сегодня замечательная погода, "
                "+ вайб(состояние)")
      case 2:
          e = -50
          a, b, c, d = (0,) * 4
          print("Сегодня тебе приснился кошмар,теперь ты боишься бабайку"
                "Весь день на стрессе(состояние ухудшилось)")
      case 3:
          c = 100
          a, b, e, d = (0,) * 4
          print("Сегодня тыувидел падающую звезду и "
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
          d = 50
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
  k=int(input(""))
  match k:
    case 1:
     student_1(th,tsks,lk,tchr,cnd,a,b,c,d,e)
     th=th+a
     tsks=tsks+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
    case 2:
     student_2(th,tsks,lk,tchr,cnd,a,b,c,d,e)
     th=th+a
     tsks=tsks+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
    case 3:
     student_3(th,tsks,lk,tchr,cnd,a,b,c,d,e)
     th=th+a
     tsks=tsks+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
  cases_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  m = random.choice(cases_1)
  match m:
      case 1:
          e = 50
          a, b, c, d = (0,) * 4
          print("Ты проснулся, а сегодня замечательная погода, "
                "+ вайб(состояние)")
      case 2:
          e = -50
          a, b, c, d = (0,) * 4
          print("Сегодня тебе приснился кошмар,теперь ты боишься бабайку"
                "Весь день на стрессе(состояние ухудшилось)")
      case 3:
          c = 100
          a, b, e, d = (0,) * 4
          print("Сегодня тыувидел падающую звезду и "
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
          d = 50
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
  k=int(input(""))
  match k:
    case 1:
     student_1(th,tsks,lk,tchr,cnd,a,b,c,d,e)
     th=th+a
     tsks=tsks+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
    case 2:
     student_2(th,tsks,lk,tchr,cnd,a,b,c,d,e)
     th=th+a
     tsks=tsks+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
    case 3:
     student_3(th,tsks,lk,tchr,cnd,a,b,c,d,e)
     th=th+a
     tsks=tsks+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
  print("Вот и подошёл к концу первый день подготовки, не переживай, шансы на победу есть"
        "вот, кстати твои показатели, с которыми ты закончил день"
        "Они тебе пригоднятся для второго дня, а пока ход переходит к твоему другу"
        "(для перехода ко второй команде нажмите enter)")
  print (th, tsks,lk,tchr,cnd)

def day_2():
  print(f"{lcl.INTRODUCTION_DAY_2} ")
  print(f"{lcl.MANIUAL_DAY_2}")
  th, tsks, lk, tchr, cnd=map(int,input().split())
  cases=[1,2,3,4,5,6,7,8,9,10]
  m = random.choice(cases)
  match m:
    case 1:
     e=50
     a,b,c,d=(0,)*4
     print("Ты проснулся, а сегодня замечательная погода, "
           "+ вайб(состояние)")
    case 2:
     e = -50
     a, b, c, d = (0,) * 4
     print("Сегодня тебе приснился кошмар,теперь ты боишься бабайку"
           "Весь день на стрессе(состояние ухудшилось)")
    case 3:
     c = 100
     a, b, e, d = (0,) * 4
     print("Сегодня тыувидел падающую звезду и "
           "загадал желание - плюс удача")
    case 4:
     print("Ты нравишься старшекурснику/старшекурснице."
           " тебе скинули расписанные билеты с полезными пометками "
           "(йоу, да ты красотка/мачо""+ теория")
     a = 80
     e, b, c, d = (0,) * 4
    case 5:
     c = -80
     d= -60
     a, b, e = (0,) * 3
     print("Рассыпать соль — к ссорам и неудачам. "
          "Твои отношения с преподавателем и удача снизились")
    case 6:
     b = 80
     a, e, c, d = (0,) * 4
     print("Ты попал на бал великих математиков, они тебе все объяснили"
          " доступным языком(тралалело тралала)")
    case 7:
     b =- 70
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
     d = 50
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

  k=int(input(""))
  match k:
    case 1:
     student_1(th, tsks, lk, tchr, cnd,a,b,c,d,e)
     th=th+a
     tsks=th+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
    case 2:
     student_2(th, tsks, lk, tchr, cnd,a,b,c,d,e)
     th=th+a
     tsks=th+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
    case 3:
     student_3(th, tsks, lk, tchr, cnd,a,b,c,d,e)
     th=th+a
     tsks=th+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
  cases_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  m = random.choice(cases_1)
  match m:
      case 1:
          e = 50
          a, b, c, d = (0,) * 4
          print("Ты проснулся, а сегодня замечательная погода, "
                "+ вайб(состояние)")
      case 2:
          e = -50
          a, b, c, d = (0,) * 4
          print("Сегодня тебе приснился кошмар,теперь ты боишься бабайку"
                "Весь день на стрессе(состояние ухудшилось)")
      case 3:
          c = 100
          a, b, e, d = (0,) * 4
          print("Сегодня тыувидел падающую звезду и "
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
          d = 50
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
  k=int(input(""))
  match k:
    case 1:
     student_1(th,tsks,lk,tchr,cnd,a,b,c,d,e)
     th=th+a
     tsks=tsks+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
    case 2:
     student_2(th,tsks,lk,tchr,cnd,a,b,c,d,e)
     th=th+a
     tsks=tsks+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
    case 3:
     student_3(th,tsks,lk,tchr,cnd,a,b,c,d,e)
     th=th+a
     tsks=tsks+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
  cases_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  m = random.choice(cases_2)
  match m:
      case 1:
          e = 50
          a, b, c, d = (0,) * 4
          print("Ты проснулся, а сегодня замечательная погода, "
                "+ вайб(состояние)")
      case 2:
          e = -50
          a, b, c, d = (0,) * 4
          print("Сегодня тебе приснился кошмар,теперь ты боишься бабайку"
                "Весь день на стрессе(состояние ухудшилось)")
      case 3:
          c = 100
          a, b, e, d = (0,) * 4
          print("Сегодня тыувидел падающую звезду и "
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
          d = 50
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
  k=int(input(""))
  match k:
    case 1:
     student_1(th,tsks,lk,tchr,cnd,a,b,c,d,e)
     th=th+a
     tsks=tsks+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
    case 2:
     student_2(th,tsks,lk,tchr,cnd,a,b,c,d,e)
     th=th+a
     tsks=tsks+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
    case 3:
     student_3(th,tsks,lk,tchr,cnd,a,b,c,d,e)
     th=th+a
     tsks=tsks+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
  cases_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  m = random.choice(cases_1)
  match m:
      case 1:
          e = 50
          a, b, c, d = (0,) * 4
          print("Ты проснулся, а сегодня замечательная погода, "
                "+ вайб(состояние)")
      case 2:
          e = -50
          a, b, c, d = (0,) * 4
          print("Сегодня тебе приснился кошмар,теперь ты боишься бабайку"
                "Весь день на стрессе(состояние ухудшилось)")
      case 3:
          c = 100
          a, b, e, d = (0,) * 4
          print("Сегодня тыувидел падающую звезду и "
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
          d = 50
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
  k=int(input(""))
  match k:
    case 1:
     student_1(th,tsks,lk,tchr,cnd,a,b,c,d,e)
     th=th+a
     tsks=tsks+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
    case 2:
     student_2(th,tsks,lk,tchr,cnd,a,b,c,d,e)
     th=th+a
     tsks=tsks+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
    case 3:
     student_3(th,tsks,lk,tchr,cnd,a,b,c,d,e)
     th=th+a
     tsks=tsks+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
  print("Закончился второй день, завтра уже экзамен, "
        "хоть выспись сегодня, завтра грандиозный день."
        "Переходим к следующей команде(нажми ener,чтобы продолжить)")
  print (th, tsks,lk,tchr,cnd)
def day_3():
  print("Не переживай, всё получится, выдохни, и шагай на экзамен, только не опоздай"
        "введи значения с второго раунда(они были даны по окончаию первого раунда<3)")
  th, tsks, lk, tchr, cnd=map(int,input().split())
  cases=[1,2,3,4,5,6,7,8,9,10]
  m = random.choice(cases)
  match m:
    case 1:
     e=50
     a,b,c,d=(0,)*4
     print("Ты проснулся, а сегодня замечательная погода, "
           "+ вайб(состояние)")
    case 2:
     e = -50
     a, b, c, d = (0,) * 4
     print("Сегодня тебе приснился кошмар,теперь ты боишься бабайку"
           "Весь день на стрессе(состояние ухудшилось)")
    case 3:
     c = 100
     a, b, e, d = (0,) * 4
     print("Сегодня тыувидел падающую звезду и "
           "загадал желание - плюс удача")
    case 4:
     print("Ты нравишься старшекурснику/старшекурснице."
           " тебе скинули расписанные билеты с полезными пометками "
           "(йоу, да ты красотка/мачо""+ теория")
     a = 80
     e, b, c, d = (0,) * 4
    case 5:
     c = -80
     d= -60
     a, b, e = (0,) * 3
     print("Рассыпать соль — к ссорам и неудачам. "
          "Твои отношения с преподавателем и удача снизились")
    case 6:
     b = 80
     a, e, c, d = (0,) * 4
     print("Ты попал на бал великих математиков, они тебе все объяснили"
          " доступным языком(тралалело тралала)")
    case 7:
     b =- 70
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
     d = 50
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

  k=int(input(""))
  match k:
    case 1:
     student_1(th, tsks, lk, tchr, cnd,a,b,c,d,e)
     th=th+a
     tsks=th+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
    case 2:
     student_2(th, tsks, lk, tchr, cnd,a,b,c,d,e)
     th=th+a
     tsks=th+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
    case 3:
     student_3(th, tsks, lk, tchr, cnd,a,b,c,d,e)
     th=th+a
     tsks=th+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
  cases_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  m = random.choice(cases_1)
  match m:
      case 1:
          e = 50
          a, b, c, d = (0,) * 4
          print("Ты проснулся, а сегодня замечательная погода, "
                "+ вайб(состояние)")
      case 2:
          e = -50
          a, b, c, d = (0,) * 4
          print("Сегодня тебе приснился кошмар,теперь ты боишься бабайку"
                "Весь день на стрессе(состояние ухудшилось)")
      case 3:
          c = 100
          a, b, e, d = (0,) * 4
          print("Сегодня тыувидел падающую звезду и "
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
          d = 50
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
  k=int(input(""))
  match k:
    case 1:
     student_1(th,tsks,lk,tchr,cnd,a,b,c,d,e)
     th=th+a
     tsks=tsks+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
    case 2:
     student_2(th,tsks,lk,tchr,cnd,a,b,c,d,e)
     th=th+a
     tsks=tsks+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
    case 3:
     student_3(th,tsks,lk,tchr,cnd,a,b,c,d,e)
     th=th+a
     tsks=tsks+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
  cases_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  m = random.choice(cases_2)
  match m:
      case 1:
          e = 50
          a, b, c, d = (0,) * 4
          print("Ты проснулся, а сегодня замечательная погода, "
                "+ вайб(состояние)")
      case 2:
          e = -50
          a, b, c, d = (0,) * 4
          print("Сегодня тебе приснился кошмар,теперь ты боишься бабайку"
                "Весь день на стрессе(состояние ухудшилось)")
      case 3:
          c = 100
          a, b, e, d = (0,) * 4
          print("Сегодня тыувидел падающую звезду и "
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
          d = 50
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
  k=int(input(""))
  match k:
    case 1:
     student_1(th,tsks,lk,tchr,cnd,a,b,c,d,e)
     th=th+a
     tsks=tsks+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
    case 2:
     student_2(th,tsks,lk,tchr,cnd,a,b,c,d,e)
     th=th+a
     tsks=tsks+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
    case 3:
     student_3(th,tsks,lk,tchr,cnd,a,b,c,d,e)
     th=th+a
     tsks=tsks+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
  cases_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  m = random.choice(cases_1)
  match m:
      case 1:
          e = 50
          a, b, c, d = (0,) * 4
          print("Ты проснулся, а сегодня замечательная погода, "
                "+ вайб(состояние)")
      case 2:
          e = -50
          a, b, c, d = (0,) * 4
          print("Сегодня тебе приснился кошмар,теперь ты боишься бабайку"
                "Весь день на стрессе(состояние ухудшилось)")
      case 3:
          c = 100
          a, b, e, d = (0,) * 4
          print("Сегодня тыувидел падающую звезду и "
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
          d = 50
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
  k=int(input(""))
  match k:
    case 1:
     student_1(th,tsks,lk,tchr,cnd,a,b,c,d,e)
     th=th+a
     tsks=tsks+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
    case 2:
     student_2(th,tsks,lk,tchr,cnd,a,b,c,d,e)
     th=th+a
     tsks=tsks+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
    case 3:
     student_3(th,tsks,lk,tchr,cnd,a,b,c,d,e)
     th=th+a
     tsks=tsks+b
     lk=lk+c
     tchr=tchr+d
     cnd=cnd+e
  print("Ну всё, ты сделал всё, что мог, немного терпения и ты узнаешь, были ли твои усилия ненапрастны,"
        " но всё равно позравляю тебя с прохождением этого нелёгкого пути")
  print (th, tsks,lk,tchr,cnd)

def win():
    th, tsks, lk, tchr, cnd \
        = map(int, input("Введите значения последнего раунда (команда 1)").split())
    sum_1=th+ tsks+ lk+ tchr+ cnd
    print("Итог:",sum_1)
    th, tsks, lk, tchr, cnd \
        = map(int, input("Введите значения последнего раунда (команда 2)").split())
    sum_2 = th + tsks + lk + tchr + cnd
    print("Итог:",sum_2)
    th, tsks, lk, tchr, cnd \
        = map(int, input("Введите значения последнего раунда (команда 3)").split())
    sum_3 = th + tsks + lk + tchr + cnd
    print("Итог:",sum_3)
    if sum_1>sum_2 and sum_3>sum_2:
        print("Студент 1, у тебя пятёрка, ты умница и выиграл этих бездельников")
        print("Студент 3, у тебя четвёрка, это тоже неплохо, но увы ты не дотянул,"
              " можно было и побольше посидеть с задачами")
        print("Студент 2, у тебя тройка, все старания коту под хвост, иди учись, впереди ещё 3 экзамена")
    elif sum_1>sum_2 and sum_2>sum_3:
        print("Студент 1, у тебя пятёрка, ты умница и выиграл этих бездельников")
        print("Студент 2, у тебя четвёрка, это тоже неплохо, но увы ты не дотянул,"
              " можно было и побольше посидеть с задачами")
        print("Студент 3, у тебя тройка, все старания коту под хвост, иди учись, впереди ещё 3 экзамена")
    elif sum_2>sum_1 and sum_1>sum_3:
        print("Студент 2, у тебя пятёрка, ты умница и выиграл этих бездельников")
        print("Студент 1, у тебя четвёрка, это тоже неплохо, но увы ты не дотянул,"
              " можно было и побольше посидеть с задачами")
        print("Студент 3, у тебя тройка, все старания коту под хвост, иди учись, впереди ещё 3 экзамена")
    elif sum_2>sum_3 and sum_3>sum_2:
        print("Студент 2, у тебя пятёрка, ты умница и выиграл этих бездельников")
        print("Студент 3, у тебя четвёрка, это тоже неплохо, но увы ты не дотянул,"
              " можно было и побольше посидеть с задачами")
        print("Студент 1, у тебя тройка, все старания коту под хвост, иди учись, впереди ещё 3 экзамена")
    elif sum_3>sum_2 and sum_2>sum_1:
        print("Студент 3, у тебя пятёрка, ты умница и выиграл этих бездельников")
        print("Студент 2, у тебя четвёрка, это тоже неплохо, но увы ты не дотянул,"
              " можно было и побольше посидеть с задачами")
        print("Студент 1, у тебя тройка, все старания коту под хвост, иди учись, впереди ещё 3 экзамена")
    elif sum_3>sum_1 and sum_1>sum_2:
        print("Студент 3, у тебя пятёрка, ты умница и выиграл этих бездельников")
        print("Студент 1, у тебя четвёрка, это тоже неплохо, но увы ты не дотянул,"
              " можно было и побольше посидеть с задачами")
        print("Студент 2, у тебя тройка, все старания коту под хвост, иди учись, впереди ещё 3 экзамена")






def main():
    day_1()
    input()
    day_1()
    input()
    day_1()
    input()
    day_2()
    input()
    day_2()
    input()
    day_2()
    input()
    day_3()
    input()
    day_3()
    input()
    day_3()
    input()
    win()

if __name__ == '__main__':
    main()
