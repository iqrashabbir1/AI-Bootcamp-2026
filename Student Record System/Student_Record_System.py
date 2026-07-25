st_name = input("Enter your name: ")
marks_Eng = int(input("Enter your English marks: "))
marks_MAths = int(input("Enter your Mathematics marks: "))
marks_Science = int(input("Enter your Science marks: "))
Total_marks = marks_Eng + marks_MAths + marks_Science
Average_marks = Total_marks / 3
print("Total Marks:", Total_marks)
print("Average Marks:", Average_marks)
if Average_marks > 50:
    print("Congratulations! You have passed.")
else:
    print("Needs Improvement.")
