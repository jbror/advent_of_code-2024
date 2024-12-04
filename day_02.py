data_input = [
[7, 6, 4, 2, 1],
[1, 2, 7, 8, 9],
[9, 7, 6, 2, 1],
[1, 3, 2, 4, 5],
[8, 6, 4, 4, 1],
[1, 3, 6, 7, 9],
]




numbers = [7, 8, 4, 2, 1]
#numbers = report1[0] < report1[1] and report1[2] < report1[0]
#check = 0


for i in range(1, len(numbers)):
    if numbers[i] < numbers[i - 1]:
        print(numbers[i])
        break
        print(numbers[i])
        print('ok')

#rules

#The levels are either all increasing or all decreasing.
#Any two adjacent levels differ by at least one and at most three.

#5 levels (row)
#6 reports (columns)
