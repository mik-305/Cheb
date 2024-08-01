grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]  # Это СПИСОК с оценками
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}                        # Это МНОЖЕСТВО студентов
students_sort = sorted(students)                         # Отсортированое МНОЖЕСТВО студентов
nom_student = 0                                          # Счетчик номера студента
ocenka_odna = ' '                                         # Одна оценка - переменная для подсчёта среднего
while nom_student <= 4:
    kol_ocenok = 1
    sred_ocenka = 0
    ocenka_all = grades[nom_student]
    print(students_sort[nom_student], ' < Все его оценки > ', grades[nom_student])
    while kol_ocenok <= len(ocenka_all):
        ocenka_odna = ocenka_all[kol_ocenok-1:kol_ocenok:1] # Извлечение одной оценки
        sred_ocenka = sred_ocenka + int(ocenka_odna.pop(0))
        kol_ocenok = kol_ocenok + 1
    nom_student = nom_student + 1
    print('Средняя оценка - ',sred_ocenka / (kol_ocenok-1))

