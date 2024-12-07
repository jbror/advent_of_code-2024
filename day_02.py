
data_input = [
[7, 6, 4, 2, 1],
[1, 2, 7, 8, 9],
[9, 7, 6, 2, 1],
[1, 3, 2, 4, 5],
[8, 6, 4, 4, 1],
[1, 3, 6, 7, 9],
]


my_list = [7,10,13, 14, 15]

is_safe = True

for i in range(len(my_list) - 1):
    if my_list[i] >= my_list[i + 1]:
        # check for duplicates and to much decrease
        if my_list[i] == my_list[i + 1] or my_list[i] - 3 > my_list[i + 1]:
            is_safe = False
            break
    elif my_list[i] + 3 < my_list[i + 1]:
        is_safe = False
        break

if is_safe:
    print("Very safe")
else:
    print("Not safe, next Chernobyl INC!")
