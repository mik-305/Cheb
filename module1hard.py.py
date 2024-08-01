grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]  # Это СПИСОК с оценками
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}                        # â® ŒŽ†…‘’‚Ž áâã¤¥­â®¢
students_sort = sorted(students)                         # Žâá®àâ¨à®¢ ­®¥ ŒŽ†…‘’‚Ž áâã¤¥­â®¢
nom_student = 0                                          # ‘ç¥âç¨ª ­®¬¥à  áâã¤¥­â 
ocenka_odna = ' '                                         # Ž¤­  ®æ¥­ª  - ¯¥à¥¬¥­­ ï ¤«ï ¯®¤áçñâ  áà¥¤­¥£®
while nom_student <= 4:
    kol_ocenok = 1
    sred_ocenka = 0
    ocenka_all = grades[nom_student]
    print(students_sort[nom_student], ' < ‚á¥ ¥£® ®æ¥­ª¨ > ', grades[nom_student])
    while kol_ocenok <= len(ocenka_all):
        ocenka_odna = ocenka_all[kol_ocenok-1:kol_ocenok:1] # ˆ§¢«¥ç¥­¨¥ ®¤­®© ®æ¥­ª¨
        sred_ocenka = sred_ocenka + int(ocenka_odna.pop(0))
        kol_ocenok = kol_ocenok + 1
    nom_student = nom_student + 1
    print('‘à¥¤­ïï ®æ¥­ª  - ',sred_ocenka / (kol_ocenok-1))

