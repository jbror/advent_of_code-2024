my_list = [1, 3, 2, 4, 5]

is_increasing = True
is_decreasing = True

for i in range(1, len(my_list)):
    if my_list[i] > my_list[i-1]:
        is_decreasing = False
    elif my_list[i] < my_list[i-1]:
        is_increasing = False

    if not is_increasing and not is_decreasing:
        break

    # this checks if the code increases or decrease by maximum of 3
    if abs(my_list[i] - my_list[i-1]) > 3:
        is_safe = False # not needed but i'm keeping this to make it clear!
        break

if is_increasing or is_decreasing:
    print("very safe")
else:
    print("Not safe, next Chernobyl INC!")
