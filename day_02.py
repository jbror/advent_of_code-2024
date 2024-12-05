
data_input = [
[7, 6, 4, 2, 1],
[1, 2, 7, 8, 9],
[9, 7, 6, 2, 1],
[1, 3, 2, 4, 5],
[8, 6, 4, 4, 1],
[1, 3, 6, 7, 9],
]



my_list = [2, 4, 9, 17, 20]

is_increasing = True
for i in range(len(my_list) - 1):
    if my_list[i] >= my_list[i + 1]:
        is_increasing = False
        print(i)
        print('not bigger')
        break
    elif my_list[i] + 3 < my_list[i + 1]:
        print(my_list[i + 1])
        print('to much')
        is_increasing = False
        break
    else:
        print('so far so good')



if is_increasing:
    print("Increasing yoho!")
else:
    print("Not increasing or to much sir!")












































#rules

#The levels are either all increasing or all decreasing.
#Any two adjacent levels differ by at least one and at most three.

#5 levels (row)
#6 reports (columns)
