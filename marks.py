import pandas
students_dict = {
    "Names" : ["Yash", "Rahul", "Kiran", "Rohit", "Sara"],
    "Marks" : [79, 82, 65, 67, 78]
}

students_marks_table = pandas.DataFrame(students_dict)

print(students_marks_table)
