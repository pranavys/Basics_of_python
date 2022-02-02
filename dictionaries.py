friend_ages = {"rolf" : 20, "anne" : 23}
friend_ages["bob"] = 28
print(friend_ages)

# List of dictionaries

# friends = [
#     {"name" : "rolf", "age" : 24}
#     {"name" : "csrd", "age" : 28}
#     {"name" : "pett", "age" : 21}
#     {"name" : "opkp", "age" : 23}
    
# ]

# print(friends[0]["name"]) 

student_marks = {"rolf" : 20, "anne" : 23}

for student, attendence in student_marks.items():
    print(f"{student} : {attendence}")

if "rolf" in student_marks:
    print(f"Rolf: {student_marks['rolf']}")
else:
    print("Rolf has not attendent the exam")

attendence_values = student_marks.values()
print(sum(attendence_values) / len(attendence_values))