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
            print(f"{lcl.CONDITION_R_1}")
        case 2:
            e = -90
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_2}")
        case 3:
            c = 100
            a, b, e, d = (0,) * 4
            print(f"{lcl.LUCK_R_1}")
        case 4:
            print(f"{THEORY_R_1}")
            a = 80
            e, b, c, d = (0,) * 4
        case 5:
            c = -80
            d = -60
            a, b, e = (0,) * 3
            print(f"{lcl.LUCK_R_2}")
        case 6:
            b = 80
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_1}")
        case 7:
            b = -70
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_2}")
        case 8:
            a = -80
            e, b, c, d = (0,) * 4
            print(f"{THEORY_R_2}")
        case 9:
            d = 90
            a, b, c, e = (0,) * 4
            print(f"{LECTURER_R_1}")
        case 10:
            d = -90
            a, b, c, e = (0,) * 4
            print(f"{LECTURER_R_2}")

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
            print(f"{lcl.CONDITION_R_3}")
        case 2:
            e = -50
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_4}")
        case 3:
            c = 100
            e = 80
            a, b, d = (0,) * 3
            print(f"{lcl.LUCK_R_3}")
        case 4:
            print(f"{THEORY_R_3}")
            a = 80
            e, b, c, d = (0,) * 4
        case 5:
            c = -80
            a, b, d, e = (0,) * 4
            print(f"{lcl.LUCK_R_4}")
        case 6:
            b = 80
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_3}")
        case 7:
            b = - 70
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_2}")
        case 8:
            a = -80
            e, b, c, d = (0,) * 4
            print(f"{THEORY_R_4}")
        case 9:
            d = 90
            a, b, c, e = (0,) * 4
            print(f"{LECTURER_R_3}")
        case 10:
            d = -90
            a, b, c, e = (0,) * 4
            print(f"{LECTURER_R_4}")
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
            print(f"{lcl.CONDITION_R_5}")
        case 2:
            e = -80
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_6}")
        case 3:
            c = 100
            a, b, e, d = (0,) * 4
            print(f"{lcl.LUCK_R_1}")
        case 4:
            print(f"{lcl.THEORY_R_1}")
            a = 80
            e, b, c, d = (0,) * 4
        case 5:
            c = -100
            a, b, d, e = (0,) * 4
            print(f"{lcl.LUCK_R_5}")
        case 6:
            b = 80
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_1}")
        case 7:
            b = -80
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_2}")
        case 8:
            a = -80
            e, b, c, d = (0,) * 4
            print(f"{lcl.THEORY_R_2}")
        case 9:
            d = 90
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_4}")
        case 10:
            d = -90
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_5}")
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
            print(f"{lcl.CONDITION_R_1}")
        case 2:
            e = -70
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_2}")
        case 3:
            c = 100
            a, b, e, d = (0,) * 4
            print(f"{lcl.LUCK_R_1}")
        case 4:
            print(f"{lcl.THEORY_R_1}")
            a = 80
            e, b, c, d = (0,) * 4
        case 5:
            c = -80
            d = -70
            a, b, e = (0,) * 3
            print(f"{lcl.LUCK_R_2}")
        case 6:
            b = 80
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_1}")
        case 7:
            b = - 70
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_2}")
        case 8:
            a = -80
            e, b, c, d = (0,) * 4
            print(f"{lcl.THEORY_R_4}")
        case 9:
            d = 70
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_1}")
        case 10:
            d = -90
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_2}")
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
            print(f"{lcl.RESULT_D1_1}")
            awns=int(input())
            match awns:
                case 1:
                 e = -80
                 b = -70
                 a, c, d = (0,) * 3
                 print(f"{lcl.DEPENDENT_1}")
                case 2:
                 b = 70
                 a, c, d, e = (0,) * 4
                 print(f"{lcl.RESULT_D1_2}")
        case 2:
            print(f"{lcl.DEPENDENT_2}")
            awns=int(input())
            match awns:
                case 1:
                 a = 100
                 b = -80
                 e, c, d = (0,) * 3
                 print(f"{lcl.RESULT_D2_1}")
                case 2:
                 b = 100
                 a = -80
                 c, d, e = (0,) * 3
                 print(f"{lcl.RESULT_D2_2}")
                case 3:
                 b = 70
                 a = 70
                 c, d, e = (0,) * 3
                 print(f"{lcl.RESULT_D2_3}")
        case 3:
            print(f"{lcl.DEPENDENT_3}")
            awns=int(input())
            match awns:
                case 1:
                 a = 90
                 b,e, c, d = (0,) * 4
                 print(f"{lcl.RESULT_D3_1}")
                case 2:
                 a = -100
                 c, d, e,b = (0,) * 4
                 print(f"{lcl.RESULT_D3_2}")
        case 4:
            print(f"{lcl.DEPENDENT_4}")
            awns=int(input())
            match awns:
                case 1:
                 a = 100
                 e = -120
                 b, c, d = (0,) * 3
                 print(f"{lcl.RESULT_D4_1}")
                case 2:
                 a, c, d, e,b = (0,) * 5
                 print(f"{lcl.RESULT_D4_2}")
        case 5:
            print(f"{lcl.DEPENDENT_5}")
            awns=int(input())
            match awns:
                case 1:
                 d = 100
                 e = -90
                 b, c, a = (0,) * 3
                 print(f"{lcl.RESULT_D5_1}")
                case 2:
                 d = -50
                 a, c, e, b = (0,) * 4
                 print(f"{lcl.RESULT_D5_2}")
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
    print(f"{lcl.CONCLUSION_DAY_1} ")
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


def day_3():
    print(f"{lcl.INTRODUCTION_DAY_3}")
    th, tsks, lk, tchr, cnd = map(int, input().split())
    cases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = random.choice(cases)
    match m:
        case 1:
            e = 50
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_11}")
        case 2:
            e = -50
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_12}"
                  "(сигма сигма боой, сигма бой, сигма бой...")
        case 3:
            c = 100
            e = 40
            a, b, d = (0,) * 3
            print(f"{lcl.LUCK_R_9}")
        case 4:
            print(f"{lcl.THEORY_R_8}")
            a = 80
            e, b, c, d = (0,) * 4
        case 5:
            c = -80
            a, b, d, e = (0,) * 4
            print(f"{lcl.LUCK_R_10}")
        case 6:
            b = 80
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_8}")
        case 7:
            b = -70
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_7}")
        case 8:
            a = -80
            e, b, c, d = (0,) * 4
            print(f"{lcl.THEORY_R_9}")
        case 9:
            d = 50
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_9}")
        case 10:
            d = -90
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_10}")

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
            print(f"{lcl.CONDITIONING_R_13}")
        case 2:
            e = -50
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITIONING_R_14}")
        case 3:
            c = 100
            e = 40
            a, b, d = (0,) * 3
            print(f"{lcl.LUCK_R_11}")
        case 4:
            print(f"{lcl.THEORY_R_10}")
            a = 80
            e, b, c, d = (0,) * 4
        case 5:
            c = -80
            a, b, d, e = (0,) * 4
            print(f"{lcl.LUCK_R_10}")
        case 6:
            b = 80
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_8}ач")
        case 7:
            b = -70
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_9}")
        case 8:
            a = -80
            e, b, c, d = (0,) * 4
            print(f"{lcl.THEORY_R_9}")
        case 9:
            d = 50
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_9}")
        case 10:
            d = -90
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_11}")

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
            print(f"{lcl.CONDITION_R_11}")
        case 2:
            e = -50
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_12}")
        case 3:
            c = 100
            a, b, d, e = (0,) * 4
            print(f"{lcl.LUCK_R_12}")
        case 4:
            print(f"{lcl.THEORY_R_11}")
            a = 80
            c = 80
            e, b, d = (0,) * 3
        case 5:
            c = -80
            a, b, d, e = (0,) * 4
            print(f"{lcl.LUCK_R_10}")
        case 6:
            b = 80
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_10}")
        case 7:
            b = -70
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_7}")
        case 8:
            a = -80
            b = -80
            e, c, d = (0,) * 3
            print(f"{lcl.TASKS_R_11}")
        case 9:
            d = 50
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_9}")
        case 10:
            d = -90
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_10}")

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
            print(f"{lcl.CONDITION_R_11}")
        case 2:
            e = -50
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_12}")
        case 3:
            c = 100
            e = 40
            a, b, d = (0,) * 3
            print(f"{lcl.LUCK_R_9}")
        case 4:
            print(f"{lcl.THEORY_R_8}")
            a = 80
            e, b, c, d = (0,) * 4
        case 5:
            c = -80
            a, b, d, e = (0,) * 4
            print(f"{lcl.LUCK_R_10}")
        case 6:
            b = 80
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_8}")
        case 7:
            b = -70
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_7}")
        case 8:
            a = -80
            e, b, c, d = (0,) * 4
            print(f"{lcl.THEORY_R_9}")
        case 9:
            d = 50
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_9}")
        case 10:
            d = -90
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_10}")

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
    print(f"{lcl.EXAM_END}")
    print(th, tsks, lk, tchr, cnd)
def win():
    th, tsks, lk, tchr, cnd \
        = map(int, input(f"{lcl.RESULTS_1}").split())
    sum_1 = th + tsks + lk + tchr + cnd
    print(f"{lcl.TOTAL}: {sum_1}")
    th, tsks, lk, tchr, cnd \
        = map(int, input(f"{lcl.RESULTS_2}").split())
    sum_2 = th + tsks + lk + tchr + cnd
    print(f"{lcl.TOTAL}: {sum_2}")
    th, tsks, lk, tchr, cnd \
        = map(int, input(f"{lcl.RESULTS_3}").split())
    sum_3 = th + tsks + lk + tchr + cnd
    print(f"{lcl.TOTAL}: {sum_3}")
    if sum_1 <= 0:
        if sum_2 <= 0:
            if sum_3 <= 0:
                print(f"{lcl.LOSER_123}")
            else:
                print(f"{lcl.LOSER_12}")
                print(f"{lcl.WINNER_3}")
        elif sum_2 > sum_3 and sum_3 > 0:
            print(f"{lcl.LOSER_1}")
            print(f"{lcl.WINNER_2}")
            print(f"{lcl.SILVER_3}")
        elif sum_2 < sum_3 and sum_3 > 0:
            print(f"{lcl.LOSER_1}")
            print(f"{lcl.WINNER_3}")
            print(f"{lcl.SILVER_2}")
        elif sum_2 == sum_3:
            print(f"{lcl.LOSER_1}")
            print(f"{lcl.WINNER_23}")

        elif sum_2 <= sum_3:
            print(f"{lcl.LOSER_12}")
        else:
            print(f"{lcl.WINNER_23}")
            print(f"{lcl.WINNER_3}")

    elif sum_2 <= 0 and sum_3 <= 0:
        print(f"{lcl.LOSER_23}")
        print(f"{lcl.WINNER_1}")
    elif sum_3 <= 0 and sum_1 <= 0:
        print(f"{lcl.LOSER_13}")
        print(f"{lcl.WINNER_2}")
    if sum_1 >= sum_2 and sum_3 >= sum_2:
        print(f"{lcl.WINNER_1}")
        print(f"{lcl.SILVER_3}")
        print(f"{lcl.CUPRUM_2}")
    elif sum_1 >= sum_2 and sum_2 >= sum_3:
        print(f"{lcl.WINNER_1}")
        print(f"{lcl.SILVER_2}")
        print(f"{lcl.CUPRUM_3}")
    elif sum_2 >= sum_1 and sum_1 >= sum_3:
        print(f"{lcl.WINNER_2}")
        print(f"{lcl.SILVER_1}")
        print(f"{lcl.CUPRUM_3}")
    elif sum_2 >= sum_3 and sum_3 >= sum_2:
        print(f"{lcl.WINNER_2}")
        print(f"{lcl.SILVER_3}")
        print(f"{lcl.CUPRUM_1}")
    elif sum_3 >= sum_2 and sum_2 >= sum_1:
        print(f"{lcl.WINNER_3}")
        print(f"{lcl.SILVER_2}")
        print(f"{lcl.CUPRUM_1}")
    elif sum_3 >= sum_1 and sum_1 >= sum_2:
        print(f"{lcl.WINNER_3}")
        print(f"{lcl.SILVER_1}")
        print(f"{lcl.CUPRUM_2}")
    elif sum_1 == sum_2 and sum_1 > sum_3:
        print(f"{lcl.WINNER_12}")
        print(f"{lcl.SILVER_3}")
    elif sum_1 == sum_2 and sum_1 < sum_3:
        print(f"{lcl.WINNER_3}")
        print(f"{lcl.SILVER_1}")
        print(f"{lcl.SILVER_2}")
    elif sum_1 == sum_3 and sum_1 > sum_2:
        print(f"{lcl.WINNER_13}")
        print(f"{lcl.SILVER_2}")
    elif sum_1 == sum_2 and sum_1 < sum_3:
        print(f"{lcl.WINNER_3}")
        print(f"{lcl.SILVER_1}")
        print(f"{lcl.SILVER_2}")
    elif sum_2 == sum_3 and sum_1 < sum_3:
        print(f"{lcl.WINNER_23}")
        print(f"{lcl.SILVER_1}")
    else:
        print(f"{lcl.WINNER_123}")

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
