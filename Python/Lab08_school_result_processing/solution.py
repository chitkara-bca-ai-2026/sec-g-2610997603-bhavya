print("=" * 55)
print("             SCHOOL RESULT PROCESSING")
print("=" * 55)

name = input("Enter Student Name : ")
roll = input("Enter Roll Number : ")

print("\n--- Enter Marks for 5 Subjects (0-100) ---")

marks = []

for i in range(1, 6):
    mark = float(input("Enter marks for Subject " + str(i) + ": "))

    if mark < 0 or mark > 100:
        print("Error: Marks should be between 0 and 100.")
        exit()

    marks.append(mark)

total = sum(marks)
percentage = (total / 500) * 100

failed = False

for mark in marks:
    if mark < 40:
        failed = True
        break

if failed:
    result = "FAIL"
    grade = "F"
    remark = "Failed in one or more subjects"

elif percentage >= 90:
    result = "PASS"
    grade = "A+"
    remark = "Outstanding"

elif percentage >= 80:
    result = "PASS"
    grade = "A"
    remark = "Excellent"

elif percentage >= 70:
    result = "PASS"
    grade = "B"
    remark = "Very Good"

elif percentage >= 60:
    result = "PASS"
    grade = "C"
    remark = "Good"

elif percentage >= 50:
    result = "PASS"
    grade = "D"
    remark = "Satisfactory"

elif percentage >= 40:
    result = "PASS"
    grade = "E"
    remark = "Pass"

else:
    result = "FAIL"
    grade = "F"
    remark = "Fail"

print("\n" + "=" * 55)
print("                 STUDENT REPORT CARD")
print("=" * 55)

print("Student Name :", name)
print("Roll Number  :", roll)
print("-" * 55)
print("Total Marks  :", total, "/ 500")
print("Percentage   :", round(percentage, 2), "%")
print("Result       :", result)
print("Grade        :", grade)
print("Remarks      :", remark)

print("=" * 55)