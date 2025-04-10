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

store1 = [120, 150, 80, 200, 130] 
store2 = [100, 140, 110, 180, 150]
pairs = list(zip(store1,store2))
max_diff = -1
diff_sum = 0
print(pairs)
for i, stores in enumerate(pairs):
    store1_prices , store2_prices = stores
    diff = abs(store1_prices-store2_prices)
    if diff > max_diff:
        max_diff = diff
        top_day = i+1
    diff_sum += diff
    if (store1_prices-store2_prices > 0):
        print(f"Store 1 had better sales on day {i+1} with diff = {diff}")

mean_diff = diff_sum/len(store1)
print(f"Mean difference is {mean_diff}")
print(f"Highest differece between 2 stores is {max_diff} on day {top_day}")


