grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]  # ��� ������ � ��������
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}                        # ��� ��������� ���������
students_sort = sorted(students)                         # �������������� ��������� ���������
nom_student = 0                                          # ������� ������ ��������
ocenka_odna = ' '                                         # ���� ������ - ���������� ��� �������� ��������
while nom_student <= 4:
    kol_ocenok = 1
    sred_ocenka = 0
    ocenka_all = grades[nom_student]
    print(students_sort[nom_student], ' < ��� ��� ������ > ', grades[nom_student])
    while kol_ocenok <= len(ocenka_all):
        ocenka_odna = ocenka_all[kol_ocenok-1:kol_ocenok:1] # ���������� ����� ������
        sred_ocenka = sred_ocenka + int(ocenka_odna.pop(0))
        kol_ocenok = kol_ocenok + 1
    nom_student = nom_student + 1
    print('������� ������ - ',sred_ocenka / (kol_ocenok-1))

