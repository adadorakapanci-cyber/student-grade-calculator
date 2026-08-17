print("=== Student Grade Calculator ===")

student_name = input("Öğrenci adı: ")
course_count = int(input("Kaç ders gireceksin? "))

total_points = 0
total_credits = 0

for i in range(course_count):
    print(f"\n--- {i + 1}. Ders ---")

    course_name = input("Ders adı: ")
    credit = float(input("Ders kredisi: "))
    midterm = float(input("Vize notu: "))
    final = float(input("Final notu: "))

    average = (midterm * 0.40) + (final * 0.60)

    if average >= 90:
        letter_grade = "AA"
        grade_point = 4.00

    elif average >= 85:
        letter_grade = "BA"
        grade_point = 3.50

    elif average >= 80:
        letter_grade = "BB"
        grade_point = 3.00

    elif average >= 75:
        letter_grade = "CB"
        grade_point = 2.50

    elif average >= 70:
        letter_grade = "CC"
        grade_point = 2.00

    elif average >= 60:
        letter_grade = "DC"
        grade_point = 1.50

    elif average >= 50:
        letter_grade = "DD"
        grade_point = 1.00

    else:
        letter_grade = "FF"
        grade_point = 0.00

    total_points += grade_point * credit
    total_credits += credit

    if average >= 50:
        status = "Geçti"
    else:
        status = "Kaldı"

    print("\n--- Ders Sonucu ---")
    print("Ders:", course_name)
    print("Ortalama:", round(average, 2))
    print("Harf Notu:", letter_grade)
    print("Katsayı:", grade_point)
    print("Durum:", status)


if total_credits > 0:
    agno = total_points / total_credits

    print("\n========================")
    print("Öğrenci:", student_name)
    print("Toplam Kredi:", total_credits)
    print("AGNO:", round(agno, 2), "/ 4.00")
    print("========================")

else:
    print("Kredi bilgisi hatalı.")