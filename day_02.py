report_list = []
report_list_copy = []
with open('input_day02.txt', 'r') as file:
    for line in file:
        numbers = line.split()
        for n in numbers:
            int_n = int(n)
            report_list_copy.append(int_n)
        report_list.append(report_list_copy)
        report_list_copy = []

data_input = report_list
safe_score = 0

for l in data_input:
    my_list = l
    is_increasing = True
    is_decreasing = True

    for i in range(1, len(my_list)):
        #print(is_increasing, is_decreasing)
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
        safe_score += 1
    else:
        print("Not safe, next Chernobyl INC!")

    print(safe_score)
