def is_even(num):
    if (num%2==0):
        print("even")
    else:
        print("not even")

names = ["Misha","Dima","Valera","Katerina","Ivan"]
for name in names:
    if (len(name)>4):
        print(name)


students = {"Аня":25, "Дима":23, "Лось":20}
avrg = sum(students.values())/len(students)
for std in students:
    if (students[std]>avrg):
        print (std)


students = {
    "Аня": {"Математика": 90, "Физика": 85, "Информатика": 95},
    "Дима": {"Математика": 88, "Физика": 80, "Информатика": 82},
    "Лена": {"Математика": 92, "Физика": 87, "Информатика": 90}
}

avg = []
for std in students:
    value = sum(students[std].values())/len(students[std])
    print(f"Average for {std} is {value}")
    avg.append(value)
print(f"Max average is {max(avg)}")

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
new_nums=set(nums)
new_nums = list(new_nums)
new_nums.sort()
print(new_nums[-2])




