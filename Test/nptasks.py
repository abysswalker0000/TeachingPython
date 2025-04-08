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


store1 = [120, 150, 90, 200, 130] 
store2 = [100, 140, 110, 180, 150]
pairs = list(zip(store1,store2))
print(pairs)
for i, stores in enumerate(pairs):
    print()