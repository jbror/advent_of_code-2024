my_list = [3,6,6,5,6]

is_increasing = True
is_decreasing = True

for i in range(1, len(my_list)):
    print(is_increasing, is_decreasing)
    if my_list[i] == my_list[i-1]:
        is_decreasing = False
        is_increasing = False
        break
    elif my_list[i] > my_list[i-1]:
        is_decreasing = False
    elif my_list[i] < my_list[i-1]:
        is_increasing = False

    if not is_increasing and not is_decreasing:
        break

    # this checks if the code increases or decrease by maximum of 3
    if abs(my_list[i] - my_list[i-1]) > 3:
        is_decreasing = False
        is_increasing = False
        is_safe = False # not needed but i'm keeping this to make it clear!
        break


if is_increasing or is_decreasing:
    print("very safe")
else:
    print("Not safe, next Chernobyl INC!")
