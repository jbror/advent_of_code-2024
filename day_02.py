data_input = [
[7, 6, 4, 2, 1],
[1, 2, 7, 8, 9],
[9, 7, 6, 2, 1],
[1, 3, 2, 4, 5],
[8, 6, 4, 4, 1],
[1, 3, 6, 7, 9],
]



"""
rules

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.

5 levels (row)
6 reports (columns)

example data

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9


for use later

with open('input_day01.txt', 'r') as file:
    for line in file:
        numbers = line.split()
        left_num = int(numbers[0])
        right_num = int(numbers[1])
        left_list.append(left_num)
        right_list.append(right_num)


"""
