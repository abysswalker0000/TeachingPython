import numpy as np

A = np.arange(1,11,1)
for a in range(len(A)):
    if A[a]%2==0:
        A[a] *=2
print(A)
print(sum(A))


purchases = {
    "Хлеб": [30, 35, 28, 32],
    "Молоко": [60, 65, 70, 55],
    "Смартфон": [15000, 14500, 15500],
    "Яблоки": [45, 50, 120, 40]
}

max_avg = -1
most_expencive = 0
for prch in purchases:
    avg = np.mean(purchases[prch])
    print(f"Mean for {prch} is {avg}")
    if avg > max_avg:
        max_avg = avg
        most_expencive = prch
print(f"Most expensive product is {most_expencive} with mean price {max_avg}")
print(f"List of products with purchase price > 100 :")
for item, prices in purchases.items():
    if any(price > 100 for price in prices):
        print(item)



grades = np.array([45, 92, 78, 55, 95, 82, 60, 48, 88, 91])
grades[grades<60] = 60
grades[grades>90] += 10
count = 0
for i in grades:
    if i > 75:
        count +=1
print(f"final grades - {grades}")
print(f"Percentage of best students - {(count/len(grades))*100}%")



students = {
    "Аня": [75, 85, 90],
    "Дима": [82, 78, 95],
    "Лена": [60, 85, 88],
    "Саша": [92, 87, 83]
}
max_score = -1
mean_grades = np.array([])
for student in students:
    student_grades = np.array(students[student])
    mark_counter = np.sum(student_grades > 80)
    student_mean = np.mean(students[student])
    print(f"Mean for {student} is {round(student_mean, 2)} with amount {mark_counter} of A+ ")
    mean_grades = np.append(mean_grades, round(student_mean, 2))
    if mark_counter > max_score:
        max_score = mark_counter
        best_student = student
print(f"Best student is {best_student} with best score = {max_score}")
print(f"Array of means - {mean_grades} wth median = {np.median(mean_grades)}")


celsius = [0, 15, 25, 30, 10, 35, -5]
fahreinheit = list(map(lambda x: x * 1.8 + 32, celsius))
print(f"Full list of fahreinheit - {fahreinheit}")
high_fahreinheit = list(filter(lambda x: x>70, fahreinheit))
print(f"List of Fahreinheit > 70 - {high_fahreinheit} with mean = {np.mean(high_fahreinheit)}")


transactions = [500, -200, 300, -50, 1000, 750, -300]
income = list(filter(lambda x: x>0, transactions))
print(f"Income list - {income}")
taxes = list(map(lambda x: x/10, income))
print(f"Tax list - {taxes}, Tax sum - {sum(taxes)}, Max tax - {max(taxes)}")